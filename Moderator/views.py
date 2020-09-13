from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from Teacher.models import *






# Create your views here.

class Home(View):
    template_name = 'home.html'
    #template_name = 'profile.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

class Create_Account(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'form_template.html'
    template_name = 'registration.html'                      

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
          
          
        """form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})"""

    def post(self, request):
        u = User()
        u.username = request.POST['username']
        u.set_password(request.POST['pass'])
        
        if request.POST['select'] == 'student':
            u.is_student = True
            my_group = Group.objects.get(name='Student')
            print(my_group.name,"student")
        else:
            my_group = Group.objects.get(name='Teacher')
            print(my_group.name,"teacher")
            u.is_teacher = True 
            
        u.save()
        user = authenticate(username=request.POST['username'], password=request.POST['pass'])
        login(request, user)
        #my_group.user_set.add(user)
        user.groups.add(my_group)
        return render(request,'profile.html')

        """form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')"""

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
           return render(request,'login.html')
    
    
    def post(self, request):
        #form = AuthenticationForm(request, data=request.POST)
        password = request.POST['password']
        username = request.POST['username']
        redirect_to = request.GET.get('next',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            print("dkfkdfj",redirect_to)
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse("moderator:home"))
            # A backend authenticated the credentials
        else:
            return render(request,'login.html',{'error':1})
            # No backend authenticated the credentials
        
        
        """if form.is_valid():
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

            return redirect(reverse('profile'))"""

class Signout(View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect(reverse('moderator:home'))


        """form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})"""
         

    """def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})"""

class About(LoginRequiredMixin, View):
    #form_class = MyForm
    #initial = {'key': 'value'}
    #template_name = 'form_template.html'
    template_name = 'about.html'
    login_url = 'moderator:login'                      

    def get(self, request, *args, **kwargs):
        """form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})"""
        return render(request,self.template_name)

class Group_View(LoginRequiredMixin, View):
    login_url = 'moderator:login' 

    def get(self, request, *args, **kwargs):
        """form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})"""
        context = {
            'permissions':Permission.objects.all()
        }
          
        return render(request,'.html',context)
    
    def post(self, request, *args, **kwargs):
        
        g = Group()
        g.name = request.POST['name']
        for i in request.POST.getlist("my_multi_select1[]"):
            g.permissions.add(Permission.objects.get(name = i))
        
        return render(request,'home.html')

class Moderator_Activity(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator').first()
        if g or self.request.user.is_superuser:
            return True
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        return render(request,'moderator-page.html')

class Add_Section(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator').first()
        if g or self.request.user.is_superuser:
            return True
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):
        context = {
            'courses':Course.objects.all()
        }
        return render(request,'create-section.html',context)

    def post(self,request,*args,**kwargs):
        
        s = Section()
        s.name = request.POST['section_name']
        s.course = Course.objects.get(title = request.POST['course'])
        s.save()
        return HttpResponseRedirect(reverse("moderator:moderator")) 

class Add_Course(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = 'moderator:login' 
    raise_exception = True
    
    def test_func(self):
        g = self.request.user.groups.filter(name = 'Moderator').first()
        if g or self.request.user.is_superuser:
            return True
    
    def handle_no_permission(self):
        return HttpResponse ('you have no permission')

    def get(self,request,*args,**kwargs):

        context ={
            'teachers':Teacher.objects.all()
        }
        return render(request,'course_create.html',context)

    def post(self,request,*args,**kwargs):
        
        c = Course()

        c.title =request.POST['course_name']
        c.teacher = User.objects.get(username = request.POST['teacher'])
        c.save()
        return HttpResponseRedirect(reverse("moderator:moderator"))


