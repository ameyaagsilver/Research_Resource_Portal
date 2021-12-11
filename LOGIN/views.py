from django.shortcuts import render

# Create your views here.


# def login(request):
#     return render(request, "signin.html")


def home(request):
    return render(request, "index-2.html")

def resources(request):
    return render(request, "books-media-list-view.html")

def signin(request):
    return render(request, "signin.html")

def services(request):
    return render(request, "services.html")
