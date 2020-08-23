from django import template
from Teacher.models import Attendance
from datetime import datetime

register = template.Library()

@register.simple_tag
def attendent(name):
    a = Attendance.objects.get(student__username = name)
    return a.count()

@register.simple_tag
def exm(id):
    e = Exam_create.objects.get(id = id)
    date_time = datetime.strptime(e.exam_starting_time, '%Y-%m-%d %H:%M:%S') - datetime.now())
    return date_time

#{% load product_tags %}
#{% calc_review_count pdt.id %}