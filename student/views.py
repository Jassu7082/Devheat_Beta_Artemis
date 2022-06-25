from django.shortcuts import render, redirect
from college.models import students
from django.contrib import messages
from college.models import ExamQp
from .forms import ExamForm2


# Create your views here.
def home(request):
    print("student login started")
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        kuser = (students.objects.filter(username=username).values())
        print(kuser)
        # user = authenticate(username=username,password=pass1)
        if kuser[0]["password"] == pass1:
            print("Login success")
            print(username + " is logged in")
            uname = kuser[0]['username']
            messages.success(request,"Hey "+uname+", Welcome")
            return render(request,'Student/home.html',{'uname':uname}) 
        else:
            print("Password Error")
            messages.error(request, "bad credentials!")
            return render(request,'Student/login.html')

    return render(request,'Student/login.html')

def portal(request):
    print("hi")
    return render(request,'Student/home.html')

def test(request):
    print("testPage ")
    if request.method == 'POST':
        print("post create exam")
        form = ExamForm2(request.POST, request.FILES)
        print(form)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            print("ho")
            form.save()
            exams = ExamQp.objects.all()
            return render(request,'Student/home.html',{'exams':exams} )
        else:
            exams = ExamQp.objects.all()
            form = ExamForm2()
            return render(request,'Student/test.html',{'exams':exams, 'form':form})

    else:
        exams = ExamQp.objects.all()
        form = ExamForm2()
        return render(request,'Student/test.html',{'exams':exams, 'form':form})
