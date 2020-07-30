# Create your views here.
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

from .tasks import * 
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta, time
from Moderator.models import *

#authentication:

"""

class Home(View):
    template_name = 'home.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

"""
"""
class Create_Account(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'form_template.html'
    template_name = 'registration.html'                      

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
          
          
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        u = User()
        u.username = request.POST['username']
        u.set_password(request.POST['pass'])
        redirect_to = next
        if request.POST['select'] == 'student':
            u.is_student = True
        else:
             u.is_teacher = True 
            
        u.save()
        user = authenticate(username=u.username, password=u.password)
        login(request, user)
        return HttpResponseRedirect(redirect_to) 

        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
"""
"""
class LoginView(View):
    
    def get(self, request, *args, **kwargs):
           return render(request,'login.html')
    
    
    def post(self, request):
        #form = AuthenticationForm(request, data=request.POST)
        password = request.POST['password']
        username = request.POST['username']
        redirect_to = request.REQUEST.get('next', '')
        user = authenticate(username=username,password=password)
        if user is not None:
             login(request, user)
             return HttpResponseRedirect(redirect_to)
            # A backend authenticated the credentials
        else:
            return render(request,'login.html',{'error':1})
            # No backend authenticated the credentials
        
        
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'survey/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)

            return redirect(reverse('profile'))

"""
"""
class Signout(View):
      #form_class = MyForm
      #initial = {'key': 'value'}
      #template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(reverse('moderator:home'))


        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
         

        def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})

"""
"""
class About(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'form_template.html'
    template_name = 'about.html'                      

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
        if request.user.is_authenticated:
            return render(request,self.template_name)
        else:
            return render(request,'login.html',{"next":'next'})

"""

"""
def click(request):
    a = Input.objects.get(id = request.GET.get('identify'))
    
    if a.language_choices=='1':
        cmd = 'clang++ '+a.title+' -o out.exe'
    elif a.language_choices=='2':
        cmd = 'clang++ '+a.title+' -o out.exe'
    elif a.language_choices=='3':
        name = a.title[:-5]
        cmd ='javac '+a.title
    elif a.language_choices=='4':
        cmd = 'python '+a.title
    else:
        cmd = ' '
    
    with tempfile.TemporaryDirectory(prefix='Codes',dir=BASE_DIR) as f:

        with open(f+'/'+a.title,'w+') as d:
            d.write(a.source_code)
            d.seek(0)
            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       cwd =f,errors='st')
            try:
                if a.language_choices=='4':
                    output,error=out.communicate(input=a.given_input,timeout=a.time_limit)
                else:
                    out.communicate(timeout=a.time_limit)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=a.time_limit)
                return HttpResponse(e)
            else:
                if a.language_choices=='1' or a.language_choices=='2':
                    cmd ='out.exe'
                if a.language_choices=='3':
                    cmd = 'java '+name
                if a.language_choices=='1' or a.language_choices=='3':
                    out = subprocess.Popen(cmd,shell=True,cwd=f,stdin = subprocess.PIPE,\
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE,errors='st')
                try:
                    output,error = out.communicate(timeout=30)               
                except subprocess.TimeoutExpired as e:
                    process = psutil.Process(out.pid).children(recursive=True)
                    for proc in process:
                        proc.kill()
                    gone, alive = psutil.wait_procs(process,timeout=a.time_limit)
                    output,error = out.communicate()
                    return HttpResponse(e)

    if output:
        s = output.split('\n')
        s.pop()
        s1 = a.given_output.split(',')
        mylist = zip(s,s1)
        context = {
                'mylist':mylist,
            }
        return render(request,'html2.html',{'b':mylist})
    else:
        return HttpResponse(error)

"""

#login
"""
from .models import Account
from .Forms.create_and_change import *
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
           
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
"""
#ckeditor
 


from .Forms.post import PostForm 

from django.views.generic.edit import CreateView 
from .models import Post 
  
class Q_Create(View): 
    
    def get(self, request, *args, **kwargs):
           
        if request.user.is_authenticated:
            return render(request,'postcreate.html',{'form':PostForm})
        else:
            return render(request,'moderator:login.html')
    
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
"""      
def add_post(request): 
    if request.method == "POST": 
        form = PostForm(request.POST) 
        if form.is_valid(): 
            post_item = form.save(commit=False) 
            post_item.save() 
        else: 
            form = PostForm() 
    return render(request, 'post_form.html', {'form': PostForm})
"""

class Problem_list(View): 
    def get(self, request, *args, **kwargs):
           
           context = {
               'posts' : Post.objects.all()
           }

           if request.user.is_authenticated:
               return render(request,'table-basic.html',context)
           else:
               return render(render,'login.html')

class Problem_show(View):
    def get(self,request,*args,**kwargs):
        context={
            'problem_id' : Post.objects.get(id = kwargs['id'])
        }

        if request.user.is_authenticated:
            return render(request,'blank-page.html',context)
        else:
            return render(request,'login.html')


class Exam_list(View):
    
    
    def get(self,request,*args,**kwargs):

        context = {
            "exams" : Exam.objects.all()
        }
        if request.user.is_authenticated:
            return render(request,'table-datatable.html',context)
        else:
            return render(request,'login.html')
    
    

class Course_list(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return render(request,'chartjs.html')
        else:
            return render(request,'login.html')
    
class Exam_create(View):
    
    def get(self,request,*args,**kwargs):
        
        context = {
            "problems":Post.objects.all()
        }

        if request.user.is_authenticated:
            return render(request,'form-pickers.html',context)
        else:
            return render(request,'login.html')
    
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

    
class Submit(View):
    def get(self,request,*args,**kwargs):
        
        if request.user.is_authenticated:
            return render(request,"form-checkbox-radio.html")
        else:
            return render(request,"login.html")

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

class Result_Show(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            r = Result.objects.all()
            print(r)
            context={
                'r':r
            }
            return render(request,"result_status.html",context)
        else:
            return render(request,"login.html")

class Report_Show(View):
    def get(self,request,*args,**kwargs):
        r = Result.objects.get(id = kwargs["id"])
        f = open(BASE_DIR+"\\"+"templates"+"\\"+"report.html","w")
        f.write(r.report)
        f.close()
        return render(request,"report.html")

class Exam_Detail(View):
    def get(self,request,*args,**kwargs):
        e = Exam.objects.get(id = kwargs["id"])
        problems = e.problem.all()
        print(e.problem.all())
        return render(request,'table-basic.html',{'problems':problems})

class Mark(View):
    def get(self,request,*args,**kwargs):
        context = {
            'u': User.objects.all()
        }

        return render(request,'marks.html',context)