from django.shortcuts import render
import subprocess
import os
from .models import *
from  Exam_System.settings import *
import tempfile
from django.http import *
import psutil
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy

#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta, time
from Moderator.models import *
from Teacher.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Teacher.tasks import *

# Create your views here.

class Course_list(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('moderator.view_course',)  
    raise_exception = True
    
    def get(self,request,*args,**kwargs):
        return render(request,'chartjs.html')
        


class Submit(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('student.add_input',)  
    raise_exception = True
    
    def get(self,request,*args,**kwargs):
        
        return render(request,"form-checkbox-radio.html")

    def post(self,request,*args,**kwargs):

        ob = Input()
        
        x = request.POST["problem_name"].split()
        title = "_".join(x)

        ob.title = title
        ob.source_code = request.POST["source_code"]
        ob.language_choices = request.POST["language"]
        

        ob.problem = Post.objects.get(Problem_Name = request.POST["problem_name"])
        ob.save()

        user_id = request.user.id
        id = ob.id
        
        compile.delay(user_id,id)
        return HttpResponse("success")


class Exam_Detail(LoginRequiredMixin,PermissionRequiredMixin, View):
    
    login_url = 'moderator:login'
    permission_required = ('teacer.view_exam',)  
    raise_exception = True

    def get(self,request,*args,**kwargs):
        e = Exam.objects.get(id = kwargs["id"])
        problems = e.problem.all()
        print(e.problem.all())
        return render(request,'table-basic.html',{'problems':problems})


class Problem_list(LoginRequiredMixin,PermissionRequiredMixin, View): 
    
    login_url = 'moderator:login'
    permission_required = ('teacher.view_post',)  
    raise_exception = True

    def get(self, request, *args, **kwargs):
           
        context = {
            'posts' : Post.objects.all()
        }

        return render(request,'table-basic.html',context)
           


class Problem_show(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('teacher.view_question',)  
    raise_exception = True
    
    def get(self,request,*args,**kwargs):
        """
        context={
            'problem_id' : Post.objects.get(id = kwargs['id'])
        }
        
        """
        q_set = Question_Set.objects.all()[0]
        q = q_set.questions
        context = {
            'set':q_set,
            'description':q.description.all(),
            'multiple':q.multipl.all(),
            'truefalse':q.truefalse.all(),
            'code':q.code.all()
        }
        

        return render(request,'temporary.html',context)

class Exam_list(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('teacher.view_exam',)  
    raise_exception = True
    
    def get(self,request,*args,**kwargs):

        context = {
            "exams" : Exam.objects.all()
        }
        return render(request,'table-datatable.html',context)
        

class Mark(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('teacher.view_marks',)  
    raise_exception = True

    def get(self,request,*args,**kwargs):
        context = {
            'u': User.objects.all()
        }

        return render(request,'marks.html',context)
