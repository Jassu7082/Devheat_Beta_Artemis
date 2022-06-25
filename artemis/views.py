from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from college.models import college, students

def home(request):
    return render(request,'home.html')

def signup(request):
    print("signup started")
    if request.method == "POST":
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        dob = request.POST['dob']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        type_ = request.POST['flexRadioDefault'] 

        if pass1 != pass2:
            messages.error(request, "Password does not match")
            return redirect('home')
        if students.objects.filter(username=username) or college.objects.filter(username=username):
            messages.error(request, "UserName already exist")
            return redirect('home')

        if type_ == "Student":
            myuser = students(username=username,first_name=f_name,last_name=l_name,dob=dob,password=pass1)
        else:
            myuser = college(username=username,first_name=f_name,last_name=l_name,dob=dob,password=pass1)
        
        myuser.save()

        messages.success(request, "Your Account has been successfully created, please check your mail to confirm")
        return redirect('home')

    return render(request,'signup.html')
