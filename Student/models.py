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

class Student(models.Model):
	student = models.ForeignKey('Moderator.User',on_delete=models.CASCADE)
	question_set = models.ManyToManyField(S_question_set)
	mark = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return "mark"+self.student.username

class Student_Exam_Registration(models.Model):
	course = models.ManyToManyField('Moderator.Course')
	session = models.PositiveIntegerField(blank=True, null=True)
	student = models.ForeignKey('Moderator.User',on_delete=models.CASCADE)
	semister = models.PositiveIntegerField(blank=True, null=True)
	department = models.CharField(max_length=255,blank = True,null = True)
	year = models.PositiveIntegerField(blank=True, null=True)
	is_drop = models.BooleanField(default=False)

	def __str__(self):
		return "registration"+self.student.username
