from django.http import HttpResponse  # type: ignore
from django.shortcuts import render # type: ignore

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def joel(request):
    return HttpResponse("hello, joel")

def robert(request):
    return HttpResponse("hello, robert")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })