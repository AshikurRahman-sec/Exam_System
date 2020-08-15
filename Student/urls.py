from django.urls import path
from .views import *

app_name = 'student'

urlpatterns = [
    path('p_list/',Problem_list.as_view(),name='problemlist'),
    path('p_detail/<int:id>/',Problem_show.as_view(),name='problemdetail'),
    path('c_list/',Course_list.as_view(),name='courselist'),
    path('e_list/',Exam_list.as_view(),name='examlist'),
    path('submit/',Submit.as_view(),name="submit"),
    path('e_detail/<int:id>',Exam_Detail.as_view(),name="examdetail"),
    path('marks/',Mark.as_view(),name="marks"),
] 