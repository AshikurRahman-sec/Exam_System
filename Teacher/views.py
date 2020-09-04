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
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin





# Create your views here.

class Teacher_Home(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'moderator:login'
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*agrs,**kwargs):
        return render(request,'teacher-page.html')

class Answer_Compare(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'moderator:login'
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')
    
    def get(self, request, *args, **kwargs):

        q_set = Question_Set.objects.get(course__title='CSE-101',title='2012')
        q = q_set.questions.order_by('no')[0]
        s_q_set = S_question_set.objects.get(course__title = q_set.course.title,title = q_set.title)
        s_q = s_q_set.questions.order_by('no')[0]

        context ={
            "q":q,
            "s_q":s_q
        }
        print(q.description.all())
        return render(request,'temporary.html',context)

class University_Problem_Create(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login'
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')
    
    def get(self, request, *args, **kwargs):

        context = {
            'description':Description.objects.all(),
            'multichoices':Multiple_Choice.objects.all(),
            'code':Code.objects.all(),
            'truefalse':True_False.objects.all()
        }

        if kwargs.get('category'):
            if kwargs['category']=='descriptive':
                return render(request,'descriptive.html')
            if kwargs['category']=='truefalse':
                return render(request,'mcq.html')
            if kwargs['category']== 'multiple choice':
                return render(request,'mcq.html')
            if kwargs['category']=='code':
                return render(request,'descriptive.html')
            if kwargs['category']=='sets':
                return render(request,'QuestionSet.html',context)
        
        return render(request,'Question_Create.html')
            
    
    def post(self, request, *args, **kwargs):


        if kwargs['category']=='descriptive':
            d = Description()
            t = Title.objects.create(title=request.POST.get('tittle'))
            d.title = t
            d.answer = request.POST.get('answer') 
            d.marks = request.POST.get('marks')

            d.save()

        if kwargs['category']=='multiple':
            d = Multiple_Choice()
            t = Title.objects.create(title=request.POST.get('title'))
            d.title = t
            d.answer = request.POST.get('answer') 
            d.marks = request.POST.get('marks')
            d.option1 = request.POST.get('option1')
            d.option2 = request.POST.get('option2')
            d.option3 = request.POST.get('option3')
            d.option4 = request.POST.get('option4')

            d.save()

        if kwargs['category']=='question_set':
            #q_set = Question_Set()
            q = Question()
            #q_set.course = "CSE-101"
            #q_set.title = "2012"
            q.part = request.POST['part']
            q.no = request.POST['no']
            q.save()
            for i in request.POST.getlist('descriptive'):
                t = Title.objects.get(title = i)
                q.description.set(t.description_set.all())
            for i in request.POST.getlist('multiple'):
                t = Title.objects.get(title = i)
                q.multipl.set(t.multiple_choice_set.all())
            for i in request.POST.getlist('code'):
                t = Title.objects.get(title = i)
                q.code.set(t.code_set.all())
            for i in request.POST.getlist('truefalse'):
                t = Title.objects.get(title = i)
                q.truefalse.set(t.true_false_set.all())

        #q_set.questions=q
        #q_set.save()

        return render(request,'Question_Create.html')
            #d = Description()
            #d.tittle = request.POST.get()

class Acm_Problem_Create(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login'
      
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')
    
    def get(self, request, *args, **kwargs):
           
        return render(request,'postcreate.html',{'form':PostForm})
        
    
    def post(self, request):
        f = PostForm(request.POST)
        p = Post()
        if f.is_valid():

            myfile = request.FILES['output_file']
            name = "_".join(request.POST.get("pn").split())
            myfile.name = name+".txt"
            fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"testcase")
            fs.save(myfile.name, myfile)

            if request.FILES.get('input_file'):
                myfile = request.FILES['input_file']
                fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"input")
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

class Exam_create(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login'  
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

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
        t = datetime.strptime(request.POST['duration'],'%H:%M:%S')
        e.exam_ending_time = str(datetime.strptime(e.exam_starting_time, '%Y-%m-%d %H:%M:%S') +timedelta(hours=t.hour, minutes=t.minute, seconds=t.second))
        e.save()
        for i in request.POST.getlist("my_multi_select1[]"):
            e.problem.add(Post.objects.get(Problem_Name = i))
        context = {
            "exams" : Exam.objects.all()
        }
        return render(request,"table-datatable.html",context)

class Report_Show(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login'   
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        r = Result.objects.get(id = kwargs["id"])
        f = open(BASE_DIR+"\\"+"templates"+"\\"+"report.html","w")
        f.write(r.report)
        f.close()
        return render(request,"report.html")

class Result_Show(LoginRequiredMixin,UserPassesTestMixin, View):

    login_url = 'moderator:login'  
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission') 

    def get(self,request,*args,**kwargs):
       
        r = Result.objects.all()
        context={
            'r':r
        }
        return render(request,"result_status.html",context)
        
class Take_Attendence(LoginRequiredMixin,UserPassesTestMixin, View):
    
    login_url = 'moderator:login'  
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

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

class Attendence(LoginRequiredMixin,UserPassesTestMixin, View):
    login_url = 'moderator:login'  
    raise_exception = True

    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator') | self.request.user.groups.filter(name = 'Teacher')
        if g or self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

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
