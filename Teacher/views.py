from django.shortcuts import render
from .Forms.post import PostForm 

import subprocess
import os
from .models import *
from  Exam_System.settings import *
import tempfile
import psutil
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy

from .tasks import * 
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta, time
from Moderator.models import *
from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.

  




class Q_Create(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('teacher.add_post',)  
    raise_exception = True
    
    def get(self, request, *args, **kwargs):
           
        return render(request,'postcreate.html',{'form':PostForm})
        
    
    def post(self, request):
        f = PostForm(request.POST)
        p = Post()
        if f.is_valid() and request.FILES['input_file'] and request.FILES['output_file']:
            myfile = request.FILES['input_file']
            
            name = "_".join(request.POST.get("pn").split())

            myfile.name = name+".txt"
            fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"input")
            fs.save(myfile.name, myfile)

            myfile = request.FILES['output_file']
            myfile.name = name+".txt"
            fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"testcase")
            fs.save(myfile.name, myfile)

            p.Problem_Name = request.POST.get("pn")
            p.Problem_Rank = request.POST.get("pr")
            p.Memory_Size = request.POST.get("ms")
            p.Time_Limit = request.POST.get("tl")
            p.Output_Limit = request.POST.get("ol")
            p.Testcase_Number = request.POST.get("tl")
            p.Testcase_Linenumber = request.POST.get("tlines")
            p.Description= f.cleaned_data["Description"]

            p.save()
        return HttpResponseRedirect(reverse('moderator:home'))


class Exam_create(LoginRequiredMixin,PermissionRequiredMixin, View):
    
    login_url = 'moderator:login' 
    permission_required = ('teacher.add_exam',)  
    raise_exception = True
    def get(self,request,*args,**kwargs):
        
        context = {
            "problems":Post.objects.all()
        }

        return render(request,'form-pickers.html',context)
    
    def post(self,request,*args,**kwargs):

        e = Exam()
        e.exam_name = request.POST.get("examename")
        e.examainer_name = request.POST.get("examiner_name")
        e.exam_starting_time = request.POST.get("starting")+" "+request.POST.get("starting_time")
        e.exam_ending_time = e.exam_starting_time
        e.save()
        for i in request.POST.getlist("my_multi_select1[]"):
            e.problem.add(Post.objects.get(Problem_Name = i))
        context = {
            "exams" : Exam.objects.all()
        }
        return render(request,"table-datatable.html",context)

class Report_Show(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login' 
    permission_required = ('teacher.add_result',)  
    raise_exception = True
    def get(self,request,*args,**kwargs):
        r = Result.objects.get(id = kwargs["id"])
        f = open(BASE_DIR+"\\"+"templates"+"\\"+"report.html","w")
        f.write(r.report)
        f.close()
        return render(request,"report.html")

class Result_Show(LoginRequiredMixin,PermissionRequiredMixin, View):

    login_url = 'moderator:login'
    permission_required = ('teacher.add_result',)  
    raise_exception = True 

    def get(self,request,*args,**kwargs):
       
        r = Result.objects.all()
        context={
            'r':r
        }
        return render(request,"result_status.html",context)
        
class Take_Attendence(LoginRequiredMixin,PermissionRequiredMixin, View):
    
    login_url = 'moderator:login'
    permission_required = ('teacher.add_attendence',)  
    raise_exception = True
    def get(self,request,*args,**kwargs):
        
        return render(request,"attendence.html",context)
    
    
    def post(self,request,*args,**kwargs):

        course = Course.objects.get(title=request.get['course_name'])
        student = User.objects.get(username=request.get['username'])
        attendence = Attendence()
        attendence.course = c
        attendence.student = student
        attendence.save()
        context ={
            'objects':Attendence.objects.filter(course_title=request.get['course_name'])
        }

        return render(request,'course_attendence.html',context)

class Attendence(LoginRequiredMixin,PermissionRequiredMixin, View):
    login_url = 'moderator:login'
    permission_required = ('teacher.add_attendence',)  
    raise_exception = True
    def get(self,request,*args,**kwargs):
        
        return render(request,'course.html')
        
    def post(self,request,*args,**kwargs):
        c = course.objects.get(title = kwargs['course_name'])
        if c.teacher[-1].username == request.user.username:
            context = {
                'course_name': kwargs['course_name'],
                'datetime': datetime.now()

            }
            return(request,'attedence_list.html',context)
        else:
            return HttpResponse('you are permitted this course')