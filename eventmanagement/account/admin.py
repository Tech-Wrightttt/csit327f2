from webbrowser import register

from django.contrib import admin
from .models import User, Teacher
from .models import Student
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)

