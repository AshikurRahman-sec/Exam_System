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
from django.contrib.auth.mixins import LoginRequiredMixin
from Teacher.tasks import *

# Create your views here.

class Course_list(LoginRequiredMixin, View):

    login_url = 'moderator:login'

    def get(self,request,*args,**kwargs):
        return render(request,'chartjs.html')
        


class Submit(LoginRequiredMixin, View):

    login_url = 'moderator:login'

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


class Exam_Detail(LoginRequiredMixin, View):
    
    login_url = 'moderator:login'

    def get(self,request,*args,**kwargs):
        e = Exam.objects.get(id = kwargs["id"])
        problems = e.problem.all()
        print(e.problem.all())
        return render(request,'table-basic.html',{'problems':problems})


class Problem_list(LoginRequiredMixin, View): 
    
    login_url = 'moderator:login'

    def get(self, request, *args, **kwargs):
           
        context = {
            'posts' : Post.objects.all()
        }

        return render(request,'table-basic.html',context)
           


class Problem_show(LoginRequiredMixin, View):

    login_url = 'moderator:login'
    
    def get(self,request,*args,**kwargs):
        context={
            'problem_id' : Post.objects.get(id = kwargs['id'])
        }

        return render(request,'blank-page.html',context)

class Exam_list(LoginRequiredMixin, View):

    login_url = 'moderator:login'
    
    def get(self,request,*args,**kwargs):

        context = {
            "exams" : Exam.objects.all()
        }
        return render(request,'table-datatable.html',context)
        

class Mark(LoginRequiredMixin, View):

    login_url = 'moderator:login'

    def get(self,request,*args,**kwargs):
        context = {
            'u': User.objects.all()
        }

        return render(request,'marks.html',context)
