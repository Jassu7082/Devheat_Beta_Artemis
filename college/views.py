from django.shortcuts import render
from college.models import college
from django.contrib import messages
from .forms import ExamForm, ResultForm
from .models import ExamQp
from student.models import ExamUpl

# Create your views here.
def home(request):
    print("College login started")
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        kuser = (college.objects.filter(username=username).values())
        print(kuser)
        if kuser[0]["password"] == pass1:
            print("Login success")
            print(username + " is logged in")
            uname = kuser[0]['username']
            exams = ExamQp.objects.all()
            messages.success(request,"Hey "+uname+", Welcome")
            print("line22")
            return render(request,'College/portal.html',{'uname':uname, 'exams':exams}) 
        else:
            print("Password Error")
            messages.error(request, "bad credentials!")
            return render(request,'College/login.html')

    return render(request,'College/login.html') 

def cportal(request):
    print("hii cportal request opened")
    exams = ExamQp.objects.all()
    return render(request,'College/portal.html',{'exams':exams})

def createxam(request):
    if request.method == 'POST':
        print("post create exam")
        form = ExamForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid:
            form.save()
            exams = ExamQp.objects.all()
            return render(request,'College/portal.html',{'exams':exams} )
    else:
        print("form created")
        form = ExamForm()
        return render(request,'College/portal1.html',{'form' : form} )


def correction(request):
    print("showing uploaded")
    exams = ExamUpl.objects.all()
    return render(request,'College/correction.html',{'exams' : exams} )

def result(request):
    print("Showing results")
    if request.method == 'POST':
        print("post result")
        form3 = ResultForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form3.is_valid:
            form3.save()
            print("saved form")
            exams = ExamQp.objects.all()
            return render(request,'College/portal.html',{'exams':exams} )
    else:
        print("form created")
        form = ResultForm()
        return render(request,'College/results.html',{'form' : form} )