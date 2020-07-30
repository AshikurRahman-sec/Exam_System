
# Create your models here.

# for taking input
from django.db import models
from django.conf import settings


from ckeditor_uploader.fields import RichTextUploadingField


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

class Input(models.Model):
	problem = models.ForeignKey(Post,on_delete=models.CASCADE)
	title = models.CharField(max_length=255,blank = True,null = True)
	source_code = models.TextField(blank=True, null=True)
	language_choices = models.CharField(max_length=255,blank=True, null=True) 
    
	def __str__ (self):
		return self.title




class Result(models.Model):

	problem = models.ForeignKey(Input,on_delete=models.CASCADE)
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





#ckeditor

#for custom user
"""from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin"""

"""class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
"""

"""class Account(AbstractBaseUser,PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
"""