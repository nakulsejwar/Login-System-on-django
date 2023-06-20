from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def HomePage(request):
    return render (request,'Home.html')

def HomePage2(request):
    return render (request,'Home2.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
       
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    

    return render (request,'signup.html')

    


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home2')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

@login_required
def HomePage2(request):
    return render (request,'Home2.html')

def LogoutPage(request):
    logout(request)
    return redirect('http://localhost:8000')



