from django.http import JsonResponse
from USERVIEW.models import resources as res
from django.shortcuts import redirect, render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from pyasn1.type.univ import Null
import pyrebase
from django.contrib import auth, messages
from django.templatetags.static import static
from django.urls import reverse
from RESEARCH_RESOURCE_PORTAL.settings import STATIC_ROOT
from USERVIEW import models
from django.contrib import auth as djAuth
from USERVIEW import models as userviewMODELS


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
                message = "Password does not match with re-entered password!!! Try again"
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
                print(user)
            except:
                message = "Invalid credentials!!! Try again"
                return render(request, 'signin.html', {"message": message})
            session_id = user['localId']
            request.session['uid'] = str(session_id)
            request.session['username'] = str(email.split('@')[0])
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
    try:
        username = request.session['username']
        print(username)
        print(request.session['uid'])
        user_id = request.session['uid']
        request.session['isAdmin'] = False

        admins = list(models.admins.objects.raw(
            'SELECT user_id FROM admins WHERE user_id = "%s"' % user_id))

        if(len(admins) == 1):
            print("It is admin")
            request.session['isAdmin'] = True
            return render(request, "index-2.html", {"username": username, "admin": "YES"})
        else:
            return render(request, "index-2.html", {"username": username})
    except:
        pass

    return render(request, "index-2.html")


def services(request):
    return render(request, "services.html")


# DISPLAYs all the resources in the database (for admin as well as to user views)
def resources(request):
    # SEARCH REDIRECTS BACK TO THE SAME URL= 'GENERIC-RES-LIST-VIEW'
    if request.method == 'POST' and (request.POST.get('keywords') or request.POST.get('resourceID') or request.POST.get('departmentName') or request.POST.get('costUpperBound') or request.POST.get('purchaseDate') or request.POST.get('costLowerBound')):
        isAdmin = False
        isUser = False
        try:
            isAdmin = request.session['isAdmin']
            username = request.session['username']
            isUser = True
        except:
            pass
        searchedQuery = {}
        resource_list1 = res.objects.none()  # declaring an empty querysert
        resource_list2 = res.objects.none()
        resource_list3 = res.objects.none()
        resource_list4 = res.objects.none()
        resource_list5 = res.objects.none()
        resource_list6 = res.objects.none()

        if request.POST.get('keywords'): # searching for list of keywords in the database
            keywords_list = request.POST.get('keywords').split(' ')
            searchedQuery['keywords'] = request.POST.get('keywords')
            for keyword in keywords_list:
                resource_list1 = resource_list1 | res.objects.filter(
                    resource_name__icontains=keyword)
        else:
            resource_list1 = res.objects.all()

        if request.POST.get('resourceID'):
            resourceID = request.POST.get('resourceID')
            searchedQuery['resourceID'] = resourceID
            resource_list2 = res.objects.filter(resource_id__iexact=resourceID)
        else:
            resource_list2 = res.objects.all()

        if request.POST.get('departmentName') != "All departments":
            departmentName = request.POST.get('departmentName')
            searchedQuery['departmentName'] = departmentName
            resource_list3 = res.objects.filter(
                department_name__icontains=departmentName)
        else:
            resource_list3 = res.objects.all()
        if isAdmin:
            print("Hllo this is admin")
            resource_list4 = res.objects.all()  # declaring an empty querysert
            # if request.POST.get('departmentName'):
            #     deptName = request.POST.get('departmentName')
            #     searchedQuery['departmentName'] = deptName
            #     resource_list4 = res.objects.filter(department_name__contains=deptName)
            # else:
            #     resource_list4 = res.objects.all()

            if request.POST.get('costUpperBound'):
                costUpperBound = request.POST.get('costUpperBound')
                print("*******", costUpperBound)
                searchedQuery['costUpperBound'] = costUpperBound
                resource_list5 = res.objects.filter(
                    unit_cost__lte=costUpperBound)
            else:
                resource_list5 = res.objects.all()
            if request.POST.get('costLowerBound'):
                costLowerBound = request.POST.get('costLowerBound')
                searchedQuery['costLowerBound'] = costLowerBound
                resource_list6 = res.objects.filter(
                    unit_cost__gte=costLowerBound)
            else:
                resource_list6 = res.objects.all()
        resource_list = resource_list1 & resource_list2 & resource_list3 & resource_list4 & resource_list5 & resource_list6
        # resource_list = resource_list[:5]
        if isAdmin:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "admin": 'YES', "searchedQuery": searchedQuery})
        elif isUser:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "searchedQuery": searchedQuery})
        else:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "searchedQuery": searchedQuery})

    resource_list = res.objects.all()
    # resource_list = resource_list[:50]
    # print(resource_list)
    try:
        username = request.session['username']
        isAdmin = request.session['isAdmin']
        if isAdmin:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "admin": "YES"})
        return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username})
    except:
        pass
    return render(request, "generic-resources-list-view.html", {"resources": resource_list})


def contact(request):
    isAdmin = False
    isUser = False
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        isUser = True
    except:
        pass
    if isAdmin:
        return render(request, "contact.html", {"username": username, "admin": 'YES'})
    elif isUser:
        return render(request, "contact.html", {"username": username})
    else:
        return render(request, "contact.html")


# return the READ MORE section of a resource selected
def readMoreAboutResource(request):
    isAdmin = False
    isUser = False
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        isUser = True
    except:
        pass
    if request.method == 'POST':
        resourceID = request.POST.get('resourceID')
        print(resourceID)
        resource_instance = get_resource_instance_by_id(resourceID)
        print(resource_instance)
        relatedLinks = userviewMODELS.resourceRelatedLinks.objects.filter(resource_id=resourceID)
        print(relatedLinks)
        if isAdmin:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks, "username": username, "admin": 'YES'})
        elif isUser:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks, "username": username})
        else:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks})

    else:
        return redirect('generic-resources-list-view')


def searchAutoCompleteEmailID(request):
    partialEmailID = request.GET.get('emailID')
    allEmails = []
    if partialEmailID:
        allEmailIDs = userviewMODELS.users.objects.filter(emailID__icontains=partialEmailID)
        for email in allEmailIDs:
            allEmails.append(email.emailID)
    return JsonResponse({'status':200, 'data':allEmails[0:3]})


def get_user_instance_by_email(email_id):
    user = userviewMODELS.users.objects.filter(emailID=email_id).first()
    return user


def get_admin_instance_by_id(adminID):
    admin = userviewMODELS.admins.objects.filter(user_id=adminID).first()
    return admin


def get_resource_instance_by_id(resourceID):
    resource = userviewMODELS.resources.objects.filter(
        resource_id=resourceID).first()
    return resource

def searchComponent(request):
    return render(request, "searchComponent.html")