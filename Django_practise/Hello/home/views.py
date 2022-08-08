from multiprocessing import context
from django.shortcuts import render , HttpResponse
from home.models import contacts 
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
        email = request.POST.get('email'),
        text = request.POST.get('text')
        contacts = contacts(email=email, text=text)
        contacts.save()
    
    return render(request,'contacts.html')
    
# Create your views here.
