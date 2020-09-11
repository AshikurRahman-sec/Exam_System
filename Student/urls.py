from django.urls import path
from .views import *

app_name = 'student'

urlpatterns = [
    path('',Student_Home.as_view(),name='studenthome'),
    path('registration/',Exam_Registration.as_view(),name='examregistration'),
    path('p_list/',Problem_list.as_view(),name='problemlist'),
    path('exam_question_show/',Exam_Problem_Show.as_view(),name='examquestionshow'),
    path('p_detail/<int:id>/',Acm_Problem_show.as_view(),name='problemdetail'),
    path('c_list/',Course_list.as_view(),name='courselist'),
    path('e_list/',Exam_list.as_view(),name='examlist'),
    path('submit/<q_set_title>/<int:no>/',Exam_Question_Submit.as_view(),name="examsubmit"),
    path('submit/',Acm_Problem_Submit.as_view(),name="acmsubmit"),
    path('e_detail/<int:id>/',Exam_Detail.as_view(),name="examdetail"),
    path('marks/',Mark.as_view(),name="marks"),
] 
