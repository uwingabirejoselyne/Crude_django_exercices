from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','LastName','Regno','email','password')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','courseName','lectureName','courseId')


class MarksAdmin(admin.ModelAdmin):
    list_display = ('id','StudentName','Regno','course')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','Regno','course','marks','subject')


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('id','Regno','attendence')


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Attendence, AttendenceAdmin)




