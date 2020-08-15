from django import template
from Teacher.models import Attendance

register = template.Library()

@register.simple_tag
def (name):
    attendance = Attendance.objects.filter(student.username=name)
    return attendance.count()


#{% load product_tags %}
#{% calc_review_count pdt.id %}