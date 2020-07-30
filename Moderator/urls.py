from django.urls import path,include
from .views import *

app_name = 'moderator'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('student/',include('Student.urls',namespace="student")),
    path('teacher/',include('Teacher.urls',namespace="teacher")),
    path('signout/',Signout.as_view(),name='Signout'),
    path('login/',LoginView.as_view(),name='login'),
    path('Create_Account/',Create_Account.as_view(),name='createaccount'),
    path('about_us/',About.as_view(),name='about'),
] 