from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	student = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='image/')
	date_of_birth = models.DateField(blank=True, null=True)
	registration_number = models.CharField(max_length=6, unique=True)
	department = models.ForeignKey('Moderator.Department', on_delete=models.CASCADE)
	mobile = models.CharField(max_length=11, blank=True, null=True)
	update = models.DateTimeField(auto_now=True)
	guardian_mobile = models.CharField(max_length=11, blank=True, null=True)
	session = models.CharField(max_length=100,null= True,blank = True)
	session = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		self.student.username
        
class Input(models.Model):
	problem = models.ForeignKey('Teacher.Post',on_delete=models.CASCADE)
	title = models.CharField(max_length=255,blank = True,null = True)
	source_code = models.TextField(blank=True, null=True)
	language_choices = models.CharField(max_length=255,blank=True, null=True) 
    
	def __str__ (self):
		return self.title

class Exam_Registration(models.Model):
	student = models.ManyToManyField(User)
	course = models.ManyToManyField('Moderator.Course')
	section = models.ManyToManyField('Moderator.Section')
	created = models.DateField(auto_now_add=True)

class Course_Registration(models.Model):
	student = models.ManyToManyField(User)
	course = models.ManyToManyField('Moderator.Course')
	section = models.ManyToManyField('Moderator.Section')
	session = models.PositiveIntegerField(blank=True, null=True)
	created = models.DateField(auto_now_add=True)

class S_description(models.Model):
	answer = models.TextField(blank = True,null = True)
	serial = models.PositiveIntegerField(blank=True, null=True)

	def __str__ (self):
		return 'description'

class S_multiple_choice(models.Model):
	answer = models.CharField(max_length=500,blank=True,null=True)
	serial = models.PositiveIntegerField(blank=True, null=True)

	def __str__ (self):
		return 'multichoice'

class S_code(models.Model):
	answer = models.TextField(blank = True,null= True)
	serial = models.PositiveIntegerField(blank=True, null=True)

	def __str__ (self):
		return 'code'

class S_truefalse(models.Model):
	answer = models.CharField(max_length=500,blank=True,null=True)
	serial = models.PositiveIntegerField(blank=True, null=True)
	
	def __str__ (self):
		return 'truefalse'

class S_question(models.Model):
	no = models.IntegerField(null = True,blank = True)
	part = models.CharField(max_length=5,blank=True,null=True)
	description = models.ManyToManyField(S_description)
	multipl = models.ManyToManyField(S_multiple_choice)
	code = models.ManyToManyField(S_code)
	truefalse = models.ManyToManyField(S_truefalse)
	
	def __str__(self):
		return str(self.no)

class S_question_set(models.Model):
	course = models.ForeignKey('Moderator.Course',on_delete=models.CASCADE)
	title = models.CharField(max_length=20,null= True,blank= True)
	questions = models.ManyToManyField(S_question)
	date_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.course.title

class Student_Mark(models.Model):
	student = models.ForeignKey(User,on_delete=models.CASCADE)
	question_set = models.ManyToManyField(S_question_set)
	mark = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return "mark"+self.student.username

class Student_Exam_Registration(models.Model):
	course = models.ManyToManyField('Moderator.Course')
	session = models.PositiveIntegerField(blank=True, null=True)
	student = models.ForeignKey(User,on_delete=models.CASCADE)
	semister = models.PositiveIntegerField(blank=True, null=True)
	department = models.CharField(max_length=255,blank = True,null = True)
	year = models.PositiveIntegerField(blank=True, null=True)
	is_drop = models.BooleanField(default=False)

	def __str__(self):
		return "registration"+self.student.username



