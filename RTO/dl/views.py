from django.shortcuts import render,redirect
from dl.models import *
from .models import User
from django.contrib import messages
from django.contrib .auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/register/')
def abc(request):
    if request.method=="POST":
        data=request.POST
        a=data.get("ename")
        b=data.get("email")
        c=data.get("address")
        d=data.get("phno")
        employee.objects.create(ename=a,email=b,address=c,phno=d)

    queryset=employee.objects.all()
    context={'emp':queryset}
    return render(request,'delete.html',context)


def delete(request,id):
    queryset=employee.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update(request,id):
    queryset=employee.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        a=data.get("ename")
        b=data.get("email")
        c=data.get("address")
        d=data.get("phno")
        queryset.ename=a
        queryset.email=b
        queryset.address=c
        queryset.phno=d
        
        queryset.save()
        return redirect('/')

    context={'del':queryset}
    return render(request,"update.html",context)

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request,"invalid username")
            return redirect("/login")
    
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"invalid passord")
            return redirect("/login")
        else:
            login(request,user)
            return redirect("/")

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/')


def register(request):

    if request.method =="POST":
        if request.method=="POST":
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            username=request.POST.get("username")
            password=request.POST.get("password")


            user=User.objects.filter(username=username)
            if user.exists():
                messages.info(request,"username already taken")
                return redirect('/register')
            # this stage user is variablle
            
            user=User.objects.create(first_name=first_name,last_name=last_name,username=username)

            user.set_password(password)
            user.save()
            messages.info(request,"account created")
            return redirect('/login')



    return render(request,'register.html')