from django.urls import path,include
from Compilation import views
from Compilation.views import *
#from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    
    path('create/',Q_Create.as_view(),name='create'),
    path('p_list/',Problem_list.as_view(),name='problemlist'),
    path('p_detail/<int:id>/',Problem_show.as_view(),name='problemdetail'),
    path('e_list/',Exam_list.as_view(),name='examlist'),
    path('c_list/',Course_list.as_view(),name='courselist'),
    path('e_create/',Exam_create.as_view(),name="examcreate"),
    path('submit/',Submit.as_view(),name="submit"),
    path('result/',Result_Show.as_view(),name= "result"),
    path('report/',Report_Show.as_view(),name="report"),
    path('e_detail/<int:id>',Exam_Detail.as_view(),name="examdetail"),
    path('marks/',Mark.as_view(),name="marks"),
    #path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('',Home.as_view(),name='home'),
    #path('signout/',Signout.as_view(),name='Signout'),
    #path('login/',LoginView.as_view(),name='login'),
    #path('Create_Account/',Create_Account.as_view(),name='createaccount'),
    #path('about_us/',About.as_view(),name='about'),
]