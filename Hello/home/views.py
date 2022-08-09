from multiprocessing import context
from django.shortcuts import render , HttpResponse
from home.models import contact
from django.contrib import messages

def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("this is service page")
    return render(request,'services.html')

def contacts(request):
    
    # return HttpResponse("this is contact page")
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        phone = contact(name=name,email=email,password=password) 
        phone.save()
        messages.success(request,'Your message has be added')
    
    return render(request,'contacts.html')
    
# Create your views here.
