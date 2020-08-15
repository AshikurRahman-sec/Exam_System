from django.db import models

# Create your models here.

class Input(models.Model):
	problem = models.ForeignKey('Teacher.Post',on_delete=models.CASCADE)
	title = models.CharField(max_length=255,blank = True,null = True)
	source_code = models.TextField(blank=True, null=True)
	language_choices = models.CharField(max_length=255,blank=True, null=True) 
    
	def __str__ (self):
		return self.title

class Exam_Registration(models.Model):
	student = models.ManyToManyField('Moderator.User')
	course = models.ManyToManyField('Moderator.Course')
	section = models.ManyToManyField('Moderator.Section')
	session = models.PositiveIntegerField(blank=True, null=True)
	created = models.DateField(auto_now_add=True)

class Course_Registration(models.Model):
	student = models.ManyToManyField('Moderator.User')
	course = models.ManyToManyField('Moderator.Course')
	section = models.ManyToManyField('Moderator.Section')
	session = models.PositiveIntegerField(blank=True, null=True)
	created = models.DateField(auto_now_add=True)