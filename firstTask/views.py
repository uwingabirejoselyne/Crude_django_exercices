from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
import datetime, time

# Create your views here.
def display(request):
    user=request.user.username
    # print(user)
    if request.user.is_authenticated:
        img=Student.objects.get(id=1).image
        data = Student.objects.all()
        dataCourse = Course.objects.all()
        values=Result.objects.all()
        attendences = Attendence.objects.all()
        
        result=[]
        for i in values:
            d = {}
            d['student']=getStudentName(i.Regno)
            d['course']=getCourseName(i.course)
            d['marks']=i.marks
            result.append(d)

        totalmark = []
        for item in attendences:
            dicti = {}
            dicti['name'] = getStudentName(item.Regno)
            dicti['total'] = totalMarks(item.Regno)
            dicti['attendence'] = item.attendence

            totalmark.append(dicti)
        print(totalmark)
        return render(request,'index.html',{'data':data,'dataCourse':dataCourse,'result':result,'totalmark':totalmark})
    else:
        return render(request,'index.html')

def getStudentName(id):
    name = Student.objects.get(Regno=id).firstName
    return name

def getCourseName(id):
    name= Course.objects.get(courseId=id).courseName
    return name


def totalMarks (id):
    data = Result.objects.all()
    total = 0 
    for  i in data:
        if i.Regno == id:
            total += i.marks
    return total


def Update():
    user = User.objects.get(id = 1)
    user.username = 'jose'
    user.save()
    # return render(request,'index.html',{'user':user})

Update()


def formCreation(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        regno = request.POST['regno']
        email = request.POST['email']
        password = request.POST['password']
        student=Student.objects.create(
            firstName=fname,
            LastName = lname,
             Regno = regno,
             email = email,
             password = password
        )
        student.save()
    data = Student.objects.all()
    return render(request,'about.html',{'data':data})

def PersonInfo(request,name):
    data = Student.objects.get(firstName=name)
    return render(request,'info.html',{'data':data})


def deleteStudent(request,id):
    pi = Student.objects.get(pk = id)
    pi.delete()
    return redirect('ab')

def updateStudent(request,id):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        regno = request.POST['regno']
        email = request.POST['email']
        password = request.POST['password']
        student=Student.objects.get(id=id)

        student.firstName=fname
        student.LastName=lname
        student.Regno=regno
        student.email= email
        student.password=password
        student.save()
        return redirect('ab')
    else:
        return render(request,'update.html')

def current_time():
    # current_time = datetime.datetime.now().strftime('%H:%M')
    # print(current_time)
    todays_date = datetime.date.today()
    print(todays_date) 
  

current_time()
# adding strftime will remove the seconds

