from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "signin.html")


def home(request):
    return render(request, "index-2.html")