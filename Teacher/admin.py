from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Title)
admin.site.register(Description)
admin.site.register(Multiple_Choice)
admin.site.register(Code)
admin.site.register(True_False)
admin.site.register(Question)
admin.site.register(Question_Set)
