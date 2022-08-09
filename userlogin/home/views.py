
from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout ,login
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='my_redirect_field')
#pwd: hello@000
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    return render(request,'index.html')


def loginUser(request):
    
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")    
        
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render (request,'login.html')
                
            
            

    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

# Create your views here.
