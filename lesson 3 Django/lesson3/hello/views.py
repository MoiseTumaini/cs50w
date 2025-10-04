
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def moise(request):
    return HttpResponse("hello, Moise!")

def brian(request):
    return HttpResponse("hello, Brian!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })