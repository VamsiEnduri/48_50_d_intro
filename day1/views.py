

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")   

def register(request):
    return  render(request,"register.html") # req, html file
def login(request):
    return  render(request,"login.html") # req, html file