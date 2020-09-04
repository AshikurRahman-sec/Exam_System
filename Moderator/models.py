from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    department = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='image/', height_field=None, width_field=None, max_length=100,null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    registration = models.BigIntegerField(null=True,blank=True)
    session = models.CharField(max_length=100,null= True,blank = True)

    def __str__(self):
        return self.username


class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=255)
    course = models.OneToOneField(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
