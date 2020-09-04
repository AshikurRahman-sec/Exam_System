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
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from Teacher.tasks import *
from django.contrib.auth.models import Group

# Create your views here.

class Student_Home(LoginRequiredMixin,View):
    login_url = 'moderator:login'

    def get(self,request,*args,**kwargs):
        return render(request,'student-page.html')  

class Course_list(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login'  
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()
        return g.name == 'Student' or g.name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        return render(request,'chartjs.html')
        
class Acm_Problem_Submit(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()[0]
        return g.name == 'Student' or g.name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        
        return render(request,"form-checkbox-radio.html")

    def post(self,request,*args,**kwargs):

        ob = Input()
        
        x = request.POST["problem_name"].split()
        title = "_".join(x)

        ob.title = title
        ob.source_code = request.POST["source_code"]
        ob.language_choices = request.POST["language"]
        
        print(Post.objects.all())
        ob.problem = Post.objects.get(Problem_Name = request.POST["problem_name"])
        ob.save()

        user_id = request.user.id
        id = ob.id
        
        compile.delay(user_id,id)
        return HttpResponse("success")

class Exam_Question_Submit(View):
    
    def get(self,request,*args,**kwargs):

        question_set = Question_Set.objects.get(title=self.kwargs["q_set_title"])
        question = question_set.questions.get(no=self.kwargs["no"])
        category = request.GET.get('category')

        context = {
            'question_set': question_set,
            'question': question
        }


        return render(request,"answer-editor.html",context)

    def post(self,request,*args,**kwargs):
        
        s,created = Student.objects.get_or_create(student = request.user)
        c = Course.objects.get(title=request.POST["q_set"])
        q_set,created = S_question_set.objects.get_or_create(course = c,title=request.POST['q_title'])

        q,created = S_question.objects.get_or_create(no = request.POST['q_no'], part = request.POST['part'])

        if request.GET.get('category') == "description":
            d = S_description.objects.create(answer = request.POST['answer'],serial=request.POST['q_id'])
            q.description.add(d)
        if request.GET.get('category') == "multiple":
            d = S_multiple_choice.objects.create(answer = request.POST['answer'],serial=request.POST['q_id'])
            q.multipl.add(d)
        if request.GET.get('category') == "code":
            d = S_code.objects.create(answer = request.POST['answer'],serial=request.POST['q_id'])
            q.code.add(d)
        if request.GET.get('category') == "truefalse":
            d = S_truefalse.objects.create(answer = request.POST['answer'],serial=request.POST['q_id'])
            q.truefalse.add(d)

        q_set.questions.add(q)
        s.question_set.add(q_set)
        return render(request,"answer-editor.html")
        
class Exam_Detail(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()
        return g.name == 'Student' or g.name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        e = Exam.objects.get(id = kwargs["id"])
        problems = e.problem.all()
        print(e.problem.all())
        return render(request,'table-basic.html',{'problems':problems})

class Problem_list(LoginRequiredMixin,UserPassesTestMixin, View): 
    
    login_url = 'moderator:login'  
    raise_exception = True
    
    def test_func(self):

        g = self.request.user.groups.filter(name = 'Student') | self.request.user.groups.filter(name = 'Teacher')

        if g:
            return True
        else:
            return False
        
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self, request, *args, **kwargs):
           
        context = {
            'posts' : Post.objects.all()
        }

        return render(request,'table-basic.html',context)
           
class Exam_Problem_Show(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login'  
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.filter(name = 'Student') | self.request.user.groups.filter(name = 'Teacher')

        if g and self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        
        q_set = Question_Set.objects.all()[0]
        context = {
            'q_set': q_set,
            'questions': q_set.questions.all()
        }

        return render(request,'answer_sheet.html',context)

class Acm_Problem_show(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login'  
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()
        return g[0].name == 'Student' or g[0].name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        context={
            'problem_id' : Post.objects.get(id = kwargs['id'])
        }
        
        
        q_set = Question_Set.objects.all()[0]
        q = q_set.questions
        context = {
            'set':q_set,
            'description':q.description.all(),
            'multiple':q.multipl.all(),
            'truefalse':q.truefalse.all(),
            'code':q.code.all()
        }
        
        
        #return render(request,'temporary.html',context)
        return render(request,'blank-page.html',context)

class Exam_list(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()
        return g.name == 'Student' or g.name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):

        context = {
            "exams" : Exam.objects.all()
        }
        return render(request,'table-datatable.html',context)
        
class Mark(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.all()
        return g.name == 'Student' or g.name == 'Teacher'
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        context = {
            'u': User.objects.all()
        }

        return render(request,'marks.html',context)
