from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length = 200)
    LastName = models.CharField(max_length = 200)
    Regno = models.IntegerField()
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/')


class Course(models.Model):
    courseName = models.CharField(max_length = 200)
    lectureName = models.CharField(max_length = 100)
    courseId = models.CharField(max_length = 100,default ="")


class Marks(models.Model):
    StudentName = models.CharField(max_length = 200)
    Regno = models.IntegerField()
    course = models.CharField(max_length = 200)


class Result(models.Model):
    Regno = models.IntegerField()
    course = models.CharField(max_length = 200)
    marks = models.IntegerField()
    subject = models.CharField(max_length =255, default = '')


class Attendence(models.Model):
    Regno = models.IntegerField()
    attendence = models.CharField(max_length = 200)