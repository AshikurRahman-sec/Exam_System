from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Designation(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=200)
    added_in = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
	teacher = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='image/')
	date_of_birth = models.DateField(blank=True, null=True)
	designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
	expertise = models.ManyToManyField(Topic, blank=True, related_name='expert_in')
	mobile = models.CharField(max_length=11, blank=True, null=True)
	update = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.teacher.username

class Title(models.Model):
	title = models.CharField(max_length=255,blank=True,null=True,unique=True)

	def __str__(self):
		return self.title

class Description(models.Model):
	
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	answer = models.TextField(blank = True,null = True)
	marks = models.IntegerField(blank = True,null = True,default = 10)

	def __str__ (self):
		return self.title.title

class Multiple_Choice(models.Model):
	
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	option1 = models.CharField(max_length=500,blank=True,null=True)
	option2 = models.CharField(max_length=500,blank=True,null=True)
	option3 = models.CharField(max_length=500,blank=True,null=True)
	option4 = models.CharField(max_length=500,blank=True,null=True)
	answer = models.CharField(max_length=500,blank=True,null=True)
	marks = models.IntegerField(blank = True,null = True,default = 10)

	def __str__ (self):
		return self.title.title

class Code(models.Model):
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	Code = models.TextField(blank = True,null= True)
	answer = models.TextField(blank = True,null= True)
	marks = models.IntegerField(blank = True,null = True,default = 10)

	def __str__ (self):
		return self.title.title

class True_False(models.Model):
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	answer = models.CharField(max_length=500,blank=True,null=True)
	marks = models.IntegerField(blank = True,null = True,default = 10)
	
	
	def __str__ (self):
		return self.title.title

class Question(models.Model):
	part = models.CharField(max_length=5,blank=True,null=True)
	no = models.IntegerField(null = True,blank = True)
	description = models.ManyToManyField(Description)
	multipl = models.ManyToManyField(Multiple_Choice)
	code = models.ManyToManyField(Code)
	truefalse = models.ManyToManyField(True_False)
	
	def __str__(self):
		return str(self.no)

class Question_Set(models.Model):
	course = models.ForeignKey('Moderator.Course',on_delete=models.CASCADE)
	title = models.CharField(max_length=20,null= True,blank= True)
	questions = models.ManyToManyField(Question)
	date_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.course.title

class Post(models.Model):
	
	Input_file_name = models.CharField(max_length=255,blank=True,null=True)
	Output_file_name = models.CharField(max_length=255,blank=True,null=True)
	Problem_Name = models.CharField(max_length=255,blank=True,null=True)
	Problem_Rank = models.CharField(max_length=255,blank=True,null=True)
	Memory_Size  =  models.FloatField(null=True, blank=True, default=None)
	Time_Limit   =  models.FloatField(null=True, blank=True, default=None)
	Output_Limit  =  models.FloatField(null=True, blank=True, default=None)
	Description = RichTextUploadingField(blank=True, null=True)
	Testcase_Number = models.IntegerField(null=True, blank=True, default=None)
	Testcase_Linenumber = models.IntegerField(null=True, blank=True, default=None)
	#body = models.TextField(blank=True,null=True)
	#order = models.IntegerField(blank=True,null=True)
	
	def __str__ (self):
		return self.Problem_Name

class Result(models.Model):

	problem = models.ForeignKey('Student.Input',on_delete=models.CASCADE)
	answer = models.CharField(max_length=255,blank=True, null=True)
	report = models.TextField(blank = True,null = True)

	def __str__ (self):
		return "result"

class Exam(models.Model):
	
	problem = models.ManyToManyField(Post)
	exam_name = models.CharField(max_length=255,blank=True, null=True)
	examainer_name = models.CharField(max_length=255,blank=True, null=True)
	exam_starting_time = models.DateTimeField()
	exam_ending_time = models.DateTimeField()

	def __str__(self):
		return exam_name

class Take_Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey('Moderator.Course', on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)

class Attendance(models.Model):
	student = models.ManyToManyField(User)
	course = models.ForeignKey('Moderator.Course', on_delete=models.DO_NOTHING)
	date = models.DateField(auto_now_add=True)



