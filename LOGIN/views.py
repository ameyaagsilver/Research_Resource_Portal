from django.shortcuts import render

# Create your views here.
def login_firebase(request):
    return render(request, "login_firebase.html")
    