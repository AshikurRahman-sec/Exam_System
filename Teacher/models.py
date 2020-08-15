from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Title(models.Model):
	title = models.CharField(max_length=500,blank=True,null=True,unique=True)

	def __str__(self):
		return self.title


class Description(models.Model):
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	answer = models.TextField(blank = True,null = True)

	def __str__ (self):
		return self.title 

class Multiple_Choice(models.Model):
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
	option1 = models.CharField(max_length=500,blank=True,null=True)
	option1 = models.CharField(max_length=500,blank=True,null=True)
	option1 = models.CharField(max_length=500,blank=True,null=True)
	option1 = models.CharField(max_length=500,blank=True,null=True)
    answer = models.CharField(max_length=500,blank=True,null=True)

	def __str__ (self):
		return self.title

class Code(models.Model):
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
	Code = models.TextField(blank = True,null= True)
    answer = models.TextField(blank = True,null= True)

	def __str__ (self):
		return self.title

class True_False(models.Model):
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
	Statements = models.CharField(max_length=500,blank=True,null=True)
	answer = models.CharField(max_length=500,blank=True,null=True)
	
	def __str__ (self):
		return self.title

class Question(models.Model):
	part = models.CharField(max_length=5,blank=True,null=True)
    no = models.IntegerField(null = True,blank = True)
    description = models.ForeignKey(Description,on_delete=models.CASCADE)
	multipl = models.ForeignKey(Multiple_Choice,on_delete=models.CASCADE)
	code = models.ForeignKey(Code,on_delete=models.CASCADE)
    truefalse = models.ForeignKey(True_False,on_delete=models.CASCADE)

    def __str__(self):
		return self.no

class Question_Set(models.Model):
	course = models.ForeignKey('Moderator.Course',on_delete=models.CASCADE)
    title = models.CharField(max_length=20,null= True,blank= True)
	questions = models.ForeignKey(Question,on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)

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


class Attendance(models.Model):
    student = models.ForeignKey('Moderator.User', on_delete=models.DO_NOTHING)
    course = models.ForeignKey('Moderator.Course', on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)


