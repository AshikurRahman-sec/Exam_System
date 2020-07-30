from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout








# Create your views here.

class Home(View):
    template_name = 'home.html'
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
        redirect_to = next
        if request.POST['select'] == 'student':
            u.is_student = True
        else:
             u.is_teacher = True 
            
        u.save()
        user = authenticate(username=u.username, password=u.password)
        login(request, user)
        return HttpResponseRedirect(redirect_to) 

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


class About(View):
      #form_class = MyForm
      #initial = {'key': 'value'}
      #template_name = 'form_template.html'
      template_name = 'about.html'                      

      def get(self, request, *args, **kwargs):
          """form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form': form})"""
          if request.user.is_authenticated:
            return render(request,self.template_name)
          else:
            return render(request,'login.html',{"next":'next'})
