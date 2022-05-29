# from logging import exception
# import re, os, email, smtplib
# from email.message import EmailMessage
# from threading import Thread
# from django.http import JsonResponse
# from USERVIEW.models import resources as res
# from django.shortcuts import redirect, render
# import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import pyrebase
from django.contrib import auth, messages
# from django.templatetags.static import static
# from django.urls import reverse
# from RESEARCH_RESOURCE_PORTAL.settings import STATIC_ROOT
# from USERVIEW import models
from django.contrib import auth as djAuth
# from USERVIEW import models as userviewMODELS


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
try:
    auth.send_password_reset_email('ameyamgonal.is19@rvce.edu.in')
except Exception as e:
    print(json.loads(e.args[1])['error']['message'])