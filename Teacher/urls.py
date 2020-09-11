from django.urls import path,include
from .views import *

app_name = 'teacher'

urlpatterns = [
    path('',Teacher_Home.as_view(),name='teacherhome'),
    path('create/<category>',University_Problem_Create.as_view(),name='create'),
    path('create/',Acm_Problem_Create.as_view(),name='acmcreate'),
    path('e_create/',Exam_create.as_view(),name="examcreate"),
    path('result/',Result_Show.as_view(),name= "result"),
    path('report/<int:id>',Report_Show.as_view(),name="report"),
    path('compare/',Answer_Compare.as_view(),name="comare"),
    path('take_attendence/<int:id>',Take_Attendence.as_view(),name="takeattendence"),
    path('create_attendence/',Attendence.as_view(),name="createattendence"),
    path('attendence_list/',Attendance_List.as_view(),name='attendecelist'),
] 
