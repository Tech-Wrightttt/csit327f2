from django.contrib import admin
from .models import User, Teacher, Specialization
from .models import Student


# Register your models here.

class SpecializationInline(admin.TabularInline):   #to show the specialization in teacher page
    model = Specialization
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    inlines = [SpecializationInline]

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher, TeacherAdmin)


