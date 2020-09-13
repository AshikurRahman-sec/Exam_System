from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=255)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.PositiveIntegerField(blank=True, null=True)
    head = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    establish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
