from django.urls import path,include
from .views import *

app_name = 'teacher'

urlpatterns = [
    path('create/',Q_Create.as_view(),name='create'),
    path('e_create/',Exam_create.as_view(),name="examcreate"),
    path('result/',Result_Show.as_view(),name= "result"),
    path('report/<int:id>',Report_Show.as_view(),name="report"),
] 