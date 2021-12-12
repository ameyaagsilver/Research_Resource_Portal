from django.shortcuts import redirect, render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from pyasn1.type.univ import Null
import pyrebase
from django.contrib import auth
from django.templatetags.static import static
from django.urls import reverse
from RESEARCH_RESOURCE_PORTAL.settings import STATIC_ROOT
from USERVIEW import models
from django.contrib import auth as djAuth

firebaseConfig = {
    "apiKey": "AIzaSyDnv29NZQkHU-As77bePEse5V_AYIunIOI",
    "authDomain": "research-resource-portal.firebaseapp.com",
    "databaseURL": "https://research-resource-portal.firebaseio.com",
    "projectId": "research-resource-portal",
    "storageBucket": "research-resource-portal.appspot.com",
    "messagingSenderId": "437072985389",
    "appId": "1:437072985389:web:a66b365ddb3aed9fa0e7a4",
    "measurementId": "G-YXKX6X0SCV"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def signup(request):
    if request.method == "POST":
        if request.POST.get('emailID') and request.POST.get('password'):
            email = request.POST.get('emailID')
            password = request.POST.get('password')
            re_entered_password = request.POST.get('re_enter_password')
            if email.split('@')[1] != "rvce.edu.in":
                message = "Not a RVCE email ID!!! Try again"
                return render(request, "signin.html", {"message": message})
            if password != re_entered_password:
                message = "Password re-entry is incorrect!!! Try again"
                return render(request, "signin.html", {"message": message})
            try:
                user = auth.create_user_with_email_and_password(
                    email, password)
            except:
                message = "Try again!!! Unable to sign you up"
                return render(request, "signin.html", {"message": message})
            print(user)
            newUserRecord = models.users()
            newUserRecord.user_id = user['localId']
            newUserRecord.emailID = request.POST.get('emailID')
            newUserRecord.first_name = request.POST.get('first_name')
            newUserRecord.middle_name = request.POST.get('middle_name')
            newUserRecord.last_name = request.POST.get('last_name')
            newUserRecord.USN = request.POST.get('USN')
            newUserRecord.department_name = "ISE"
            newUserRecord.phone_no = request.POST.get('phone_number')
            newUserRecord.save()
            return redirect(reverse('home'))
    return render(request, "signin.html")


def signin(request):
    if request.method == "POST":
        if request.POST.get('emailID') and request.POST.get('password'):
            email = request.POST.get('emailID')
            password = request.POST.get('password')
            if email.split('@')[1] != "rvce.edu.in":
                message = "Not a RVCE email ID!!! Try again"
                return render(request, "signin.html", {"message": message})
            try:
                user = auth.sign_in_with_email_and_password(email, password)
            except:
                message = "Invalid credentials!!! Try again"
                return render(request, 'signin.html', {"message": message})
            print(user)
            session_id = user['localId']
            request.session['uid'] = str(session_id)
            request.session['username'] = str(email.split('@')[0])
            print(request.session['username'])
            return redirect('home')
    return render(request, "signin.html")


def logout(request):
    djAuth.logout(request)
    try:
        del request.session['uid']
        del request.session['username']
    except:
        pass
    return redirect(reverse('home'))


def home(request):
    # r = models.resources()
    # r.about = "dddd"
    # r.department_name = "ISe"
    # r.resource_name = "Arduino"
    # r.resource_type = "SO"
    # r.location = "Room 120 si"
    # r.image = "r.png"
    # r.quantity = 1
    # r.unit_cost = 0
    # r.OEM = "HPE"
    # r.adminId = "ergh3reu3r"
    # r.save()
    try:
        username = request.session['username']
        print(request.session['uid'])
        return render(request, "index-2.html", {"username": username})
    except:
        pass

    return render(request, "index-2.html")


def services(request):
    return render(request, "services.html")
