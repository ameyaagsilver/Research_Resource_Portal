import json
from logging import exception
import re, os, email, smtplib
from email.message import EmailMessage
from threading import Thread
from django.http import JsonResponse
from USERVIEW.models import resources as res
from django.shortcuts import redirect, render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
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
                messages.info(request, message)
                return render(request, "signin.html")
            if password != re_entered_password:
                message = "Password does not match with re-entered password!!! Try again"
                messages.info(request, message)
                return render(request, "signin.html")
            try:
                user = auth.create_user_with_email_and_password(
                    email, password)
            except:
                message = "Try again!!! Unable to sign you up"
                messages.info(request, message)
                return render(request, "signin.html")
            print(user)
            newUserRecord = models.users()
            newUserRecord.user_id = user['localId']
            newUserRecord.emailID = request.POST.get('emailID')
            newUserRecord.first_name = request.POST.get('first_name')
            newUserRecord.middle_name = request.POST.get('middle_name')
            newUserRecord.last_name = request.POST.get('last_name')
            newUserRecord.USN = request.POST.get('USN')
            newUserRecord.department_name = request.POST.get('departmentName')
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
                messages.info(request, "Not a RVCE email ID!!! Try again")
                return redirect('signin')
            try:
                user = auth.sign_in_with_email_and_password(email, password)
            except Exception as e:
                print(e)
                messages.info(request, "Invalid sign in attempt!!! Try again")
                return redirect('signin')
            session_id = user['localId']
            request.session['uid'] = str(session_id)
            request.session['username'] = str(email.split('@')[0])
            return redirect('home')
    return render(request, "signin.html")


def resetPassword(request):
    if request.method == "POST" and request.POST.get('emailID'):
        emailID = request.POST.get('emailID')
        try:
            auth.send_password_reset_email(emailID)
            messages.info(request, "Mail sent for reset password")
        except Exception as e:
            # print(e)
            if json.loads(e.args[1])['error']['message'] == 'EMAIL_NOT_FOUND':
                messages.info(request, "Email ID does not exist...Try with a valid email ID")
            messages.info(request, "Unable to reset your password...")
            return redirect("home")
    return redirect("home")


def logout(request):
    djAuth.logout(request)
    # try:
    #     del request.session['uid']
    #     del request.session['username']
    #     del request.session['isAdmin']
    # except:
    #     pass
    return redirect(reverse('signin'))


def home(request):
    portalGlobalInformation = {}
    try:
        users = list(models.users.objects.raw('SELECT * FROM users'))
        portalGlobalInformation['users'] = len(users)
        admins = list(models.admins.objects.raw('SELECT * FROM admins'))
        portalGlobalInformation['admins'] = len(admins)
        resources = list(models.resources.objects.raw('SELECT * FROM resources'))
        portalGlobalInformation['resources'] = len(resources)
    except:
        pass
    try:
        username = request.session['username']
        # print(username)
        # print(request.session['uid'])
        user_id = request.session['uid']
        request.session['isAdmin'] = False

        admins = list(models.admins.objects.raw(
            'SELECT admin_id FROM admins WHERE admin_id = "%s"' % user_id))

        if(len(admins) == 1):
            # print("It is admin")
            request.session['isAdmin'] = True
            return render(request, "index-2.html", {"username": username, "admin": "YES", "portalGlobalInformation":portalGlobalInformation})
        else:
            return render(request, "index-2.html", {"username": username, "portalGlobalInformation":portalGlobalInformation})
    except:
        pass

    return render(request, "index-2.html", {"portalGlobalInformation":portalGlobalInformation})


def services(request):
    return render(request, "services.html")

# DISPLAYs all the resources in the database (for admin as well as to user views) along with the SEARCH feature
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
            print(keywords_list)
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
        if True:
            # print("Hllo this is admin")
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
        # resource_list = resource_list[:10]
        print(resource_list2)
        if isAdmin:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "admin": 'YES', "searchedQuery": searchedQuery})
        elif isUser:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "searchedQuery": searchedQuery})
        else:
            return render(request, "generic-resources-list-view.html", {"resources": resource_list, "searchedQuery": searchedQuery})

    resource_list = res.objects.all()
    # resource_list = resource_list[:10]
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
    user_id = None
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        user_id = request.session['uid']
        isUser = True
    except:
        pass
    if request.method == "POST" and isUser:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        message = request.POST.get('message')
        phone_no = request.POST.get('phone_no')
        emailID = request.POST.get('emailID')
        new_user_message_instance = userviewMODELS.userMessage()
        # new_user_message_instance.first_name = first_name
        # new_user_message_instance.last_name = last_name
        new_user_message_instance.message = message
        # new_user_message_instance.phone_no = phone_no
        # new_user_message_instance.emailID = emailID
        new_user_message_instance.user_id = get_user_instance_by_id(user_id)
        new_user_message_instance.save()
        # sendMessageThroughMail('rvce.resource.portal@gmail.com','rvce.resource.portal@gmail.com', request)
        print("*********************")
        threadAddResource = Thread(target=sendMessageThroughMail, args=('rvce.resource.portal@gmail.com','rvce.resource.portal@gmail.com', request))
        threadAddResource.start()
        print("*********************")
        messages.info(request, "Message sent successfully!!!")
        return redirect('contact')
    elif request.method == 'POST':
        messages.info(request, "Signin before sending a message!!!")
        return redirect('signin')
    userDetails = get_user_instance_by_id(user_id)
    if isAdmin:
        return render(request, "contact.html", {"userDetails":userDetails, "username": username, "admin": 'YES'})
    elif isUser:
        return render(request, "contact.html", {"userDetails":userDetails, "username": username})
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
        # print(resourceID)
        resource_instance = get_resource_instance_by_id(resourceID)
        # print(resource_instance)
        relatedLinks = userviewMODELS.resourceRelatedLinks.objects.filter(resource_id=resourceID)
        # print(relatedLinks)
        recentlyViewedResources = None
        if 'recentlyViewedResources' in request.session:
            if int(resourceID) in request.session['recentlyViewedResources']:
                request.session['recentlyViewedResources'].remove(int(resourceID))
            recentlyViewedResources = userviewMODELS.resources.objects.filter(resource_id__in=request.session['recentlyViewedResources'])
            recentlyViewedResources = sorted(recentlyViewedResources, 
                key=lambda x: request.session['recentlyViewedResources'].index(x.resource_id)
                )
            request.session['recentlyViewedResources'].insert(0, int(resourceID))
            if len(request.session['recentlyViewedResources'])>5:
                request.session['recentlyViewedResources'].pop()
        else:
            request.session['recentlyViewedResources'] = [int(resourceID)]
        request.session.modified = True

        print((request.session['recentlyViewedResources'][0]))
        print(recentlyViewedResources)

        if isAdmin:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks, "recentlyViewedResources": recentlyViewedResources, "username": username, "admin": 'YES'})
        elif isUser:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks, "recentlyViewedResources": recentlyViewedResources, "username": username})
        else:
            return render(request, "read-more-about-resource.html", {"resource": resource_instance, "relatedLinks":relatedLinks, "recentlyViewedResources": recentlyViewedResources})

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


def userProfile(request):
    isAdmin = False
    isUser = False
    try:
        username = request.session['username']
        isUser = True
        isAdmin = request.session['isAdmin']
    except:
        pass

    if request.method == "POST":
        user_id = request.session['uid']
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        department_name = request.POST.get('department_name')
        if isAdmin:
          admin_location = request.POST.get('admin_location')
        else:
          USN = request.POST.get('USN')
        # print(first_name, middle_name, last_name, phone_no, department_name, USN)
        if isAdmin:
            admin_instance = get_admin_instance_by_id(user_id)
            # print(user_instance)
            admin_instance.first_name = first_name
            admin_instance.middle_name = middle_name
            admin_instance.last_name = last_name
            admin_instance.phone_no = phone_no
            admin_instance.department_name = department_name
            admin_instance.admin_location = admin_location
            admin_instance.save()
        else:
            user_instance = get_user_instance_by_id(user_id)
            # print(user_instance)
            user_instance.first_name = first_name
            user_instance.middle_name = middle_name
            user_instance.last_name = last_name
            user_instance.phone_no = phone_no
            user_instance.department_name = department_name
            user_instance.USN = USN
            user_instance.save()
        messages.info(request, "New profile changes saved!!!")
        return redirect(reverse('user-profile'))
    user_profile = None
    recent_issued_resources = None
    if isUser:
        userID = request.session['uid']
        user_profile = userviewMODELS.users.objects.filter(user_id=userID).first()
        recent_issued_resources = userviewMODELS.resources.objects.raw('''
        select * from resource_logbook
        join resources on resource_logbook.resource_id = resources.resource_id
        inner join admins on resource_logbook.admin_id = admins.admin_id
        where resource_logbook.member_id = "%s" and resource_logbook.return_date is null
        order by resource_logbook.issue_date desc
        limit 4
        '''%userID)
        for r in recent_issued_resources:
            print(r)
        '''
        select * from resource_logbook
        inner join resources on resource_logbook.resource_id = resources.resource_id
        inner join users on resource_logbook.member_id = users.user_id
        where return_date is null;
        '''
    if isAdmin:
        userID = request.session['uid']
        user_profile = userviewMODELS.admins.objects.filter(admin_id=userID).first()
        recent_issued_resources = userviewMODELS.resources.objects.raw('''
        select * from resource_logbook
        join resources on resource_logbook.resource_id = resources.resource_id
        inner join admins on resource_logbook.admin_id = admins.admin_id
        where resource_logbook.member_id = "%s" and resource_logbook.return_date is null
        order by resource_logbook.issue_date desc
        limit 4
        '''%userID)
    if isAdmin:
            return render(request, "user-profile.html", {"recentIssuedResources":recent_issued_resources,"userprofile": user_profile, "username": username, "admin": 'YES'})
    elif isUser:
        return render(request, "user-profile.html", {"recentIssuedResources":recent_issued_resources, "userprofile": user_profile, "username": username})
    else:
        return redirect('signin')
    

def sendMessageThroughMail(From, To, request):
    EMAIL_PASSWORD = 'Research@rvce'
    # print("EMAIL_PASSWORD", EMAIL_PASSWORD)
    Subject = 'Grievance - New message from {usersName}'.format(usersName=request.POST.get('first_name')+" "+request.POST.get('last_name'))
    Message = request.POST.get('message')
    mssg = EmailMessage()
    mssg['Subject'] = Subject
    mssg['From'] = From
    mssg['To'] = To
    mssg.set_content(Message)
    mssg.add_alternative("""\n
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Email html</title>

  <style type="text/css">
  /* Take care of image borders and formatting */

  img {
    max-width: 600px;
    outline: none;
    text-decoration: none;
    -ms-interpolation-mode: bicubic;
  }

  a {
    border: 0;
    outline: none;
  }

  a img {
    border: none;
  }

  /* General styling */

  td, h1, h2, h3  {
    font-family: Helvetica, Arial, sans-serif;
    font-weight: 400;
  }

  td {
    font-size: 13px;
    line-height: 150%;
    text-align: left;
  }

  body {
    -webkit-font-smoothing:antialiased;
    -webkit-text-size-adjust:none;
    width: 100%;
    height: 100%;
    color: #37302d;
    background: #ffffff;
  }

  table {
    border-collapse: collapse !important;
  }


  h1, h2, h3 {
    padding: 0;
    margin: 0;
    color: #444444;
    font-weight: 400;
    line-height: 110%;
  }

  h1 {
    font-size: 35px;
  }

  h2 {
    font-size: 30px;
  }

  h3 {
    font-size: 24px;
  }

  h4 {
    font-size: 18px;
    font-weight: normal;
  }

  .important-font {
    color: #21BEB4;
    font-weight: bold;
  }

  .hide {
    display: none !important;
  }

  .force-full-width {
    width: 100% !important;
  }

  td.desktop-hide {
    font-size: 0;
    height: 0;
    display: none;
    color: #ffffff;
  }


  </style>

  <style type="text/css" media="screen">
      @media screen {
        @import url(http://fonts.googleapis.com/css?family=Open+Sans:400);

        /* Thanks Outlook 2013! */
        td, h1, h2, h3 {
          font-family: 'Open Sans', 'Helvetica Neue', Arial, sans-serif !important;
        }
      }
  </style>

  <style type="text/css" media="only screen and (max-width: 600px)">
    /* Mobile styles */
    @media only screen and (max-width: 600px) {

      table[class="w320"] {
        width: 320px !important;
      }

      table[class="w300"] {
        width: 300px !important;
      }

      table[class="w290"] {
        width: 290px !important;
      }

      td[class="w320"] {
        width: 320px !important;
      }

      td[class~="mobile-padding"] {
        padding-left: 14px !important;
        padding-right: 14px !important;
      }

      td[class*="mobile-padding-left"] {
        padding-left: 14px !important;
      }

      td[class*="mobile-padding-right"] {
        padding-right: 14px !important;
      }

      td[class*="mobile-block"] {
        display: block !important;
        width: 100% !important;
        text-align: left !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        padding-bottom: 15px !important;
      }

      td[class*="mobile-no-padding-bottom"] {
        padding-bottom: 0 !important;
      }

      td[class~="mobile-center"] {
        text-align: center !important;
      }

      table[class*="mobile-center-block"] {
        float: none !important;
        margin: 0 auto !important;
      }

      *[class*="mobile-hide"] {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
        line-height: 0 !important;
        font-size: 0 !important;
      }

      td[class*="mobile-border"] {
        border: 0 !important;
      }

      td[class*="desktop-hide"] {
        display: block !important;
        font-size: 13px !important;
        height: 61px !important;
        padding-top: 10px !important;
        padding-bottom: 10px !important;
        color: #444444 !important;
      }
    }
  </style>
</head>
<body class="body" style="padding:0; margin:0; display:block; background:white; -webkit-text-size-adjust:none" bgcolor="#ffffff">
<table align="center" cellpadding="0" cellspacing="0" width="100%" height="100%">
  <tr>
    <td align="center" valign="top" bgcolor="#ffffff"  width="100%">

    <table cellspacing="0" cellpadding="0" width="100%">
      <tr>
        <td style="background:#1f1f1f" width="100%">
          <center>
            <table cellspacing="0" cellpadding="0" width="600" class="w320">
              <tr>
                <td valign="top" class="mobile-block mobile-no-padding-bottom mobile-center" width="270" style="background:#fff;padding:10px 10px 10px 20px;">
                  <a href="#" style="text-decoration:none;">
                    <h3 style="
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    ">RESEARCH RESOURCE PORTAL</h3>
                  </a>
                </td>
                <td valign="top" class="mobile-block mobile-center" width="270" style="background:#fff;padding:10px 15px 10px 10px">
                  <table border="0" cellpadding="0" cellspacing="0" class="mobile-center-block" align="right">
                    <tr>
                      <!-- <td align="right">
                        <a href="#">
                        <img src="http://keenthemes.com/assets/img/emailtemplate/social_facebook.png"  width="30" height="30" alt="social icon"/>
                        </a>
                      </td>
                      <td align="right" style="padding-left:5px">
                        <a href="#">
                        <img src="http://keenthemes.com/assets/img/emailtemplate/social_twitter.png"  width="30" height="30" alt="social icon"/>
                        </a>
                      </td>
                      <td align="right" style="padding-left:5px">
                        <a href="#">
                        <img src="http://keenthemes.com/assets/img/emailtemplate/social_googleplus.png"  width="30" height="30" alt="social icon"/>
                        </a>
                      </td>
                      <td align="right" style="padding-left:5px">
                        <a href="#">
                        <img src="http://keenthemes.com/assets/img/emailtemplate/social_linkedin.png"  width="30" height="30" alt="social icon"/>
                        </a>
                      </td>
                      <td align="right" style="padding-left:5px">
                        <a href="#">
                        <img src="http://keenthemes.com/assets/img/emailtemplate/social_rss.png"  width="30" height="30" alt="social icon"/>
                        </a>
                      </td> -->
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </center>
        </td>
      </tr>
      <tr>
        <td style="border-bottom:1px solid #e7e7e7;">
          <center>
            <table cellpadding="0" cellspacing="0" width="600" class="w320">
              <tr>
                <td align="left" class="mobile-padding" style="padding:20px">

                  <br class="mobile-hide" />

                  <div>
                    <b>""" + request.POST.get('first_name') + " " + request.POST.get('last_name') +"""</b>
                    <br>
                    Email-id : """ + request.POST.get('emailID') + """
                    <br>
                    
                    <br>
                    Phone: """ + request.POST.get('phone_no') +  """<br>
                    <br>
                    """ + request.POST.get('message') + """
                  </div>

                  <br>

                  <table cellspacing="0" cellpadding="0" width="100%" bgcolor="#ffffff">
                    <tr>
                      <td style="width:100px;background:#D84A38;">
                        <div>
                          <!--[if mso]>
                          <v:rect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="#" style="height:33px;v-text-anchor:middle;width:100px;" stroke="f" fillcolor="#D84A38">
                            <w:anchorlock/>
                            <center>
                          <![endif]-->
                              <a href="#"
                        style="background-color:#D84A38;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:33px;text-align:center;text-decoration:none;width:100px;-webkit-text-size-adjust:none;">My Account</a>
                          <!--[if mso]>
                            </center>
                          </v:rect>
                          <![endif]-->
                        </div>
                      </td>
                      <td width="281" style="background-color:#ffffff; font-size:0; line-height:0;">&nbsp;</td>
                    </tr>
                  </table>
                </td>
                <td class="mobile-hide" style="padding-top:20px;padding-bottom:0; vertical-align:bottom;" valign="bottom">
                  <table cellspacing="0" cellpadding="0" width="100%">
                    <tr>
                      <td align="right" valign="bottom" style="padding-bottom:0; vertical-align:bottom;">
                        <img  style="vertical-align:bottom;" src="https://www.filepicker.io/api/file/9f3sP1z8SeW1sMiDA48o"  width="174" height="294" />
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </center>
        </td>
      </tr>
      <tr>
        <td valign="top" style="background-color:#f8f8f8;border-bottom:1px solid #e7e7e7;">
<!-- 
          <center>
            <table border="0" cellpadding="0" cellspacing="0" width="600" class="w320" style="height:100%;">
              <tr>
                <td valign="top" class="mobile-padding" style="padding:20px;">
                  <table cellspacing="0" cellpadding="0" width="100%">
                    <tr>
                      <td style="padding-right:20px">
                        <b>Plan</b>
                      </td>
                      <td style="padding-right:20px">
                        <b>Period</b>
                      </td>
                      <td>
                        <b>Amount</b>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding-top:5px;padding-right:20px; border-top:1px solid #E7E7E7; ">
                        Silver Monthly
                      </td>
                      <td style="padding-top:5px;padding-right:20px; border-top:1px solid #E7E7E7;">
                        Dec 4, 2013 - Jan 4, 2014
                      </td>
                      <td style="padding-top:5px; border-top:1px solid #E7E7E7;" class="mobile">
                        $160.00
                      </td>
                    </tr>
                  </table>
                  <table cellspacing="0" cellpadding="0" width="100%">
                    <tr>
                      <td style="padding-top:35px;">
                        <table cellpadding="0" cellspacing="0" width="100%">
                          <tr>
                            <td width="350" class="mobile-hide" style="vertical-align:top;">
                              Thank you for your business. Please  <a href="#">contact us</a> with any questions regarding your order,<br>
                              <h4>Awesome Co<h4>
                            </td>
                            <td style="padding:0px 0 15px 30px;" class="mobile-block">
                              <table cellspacing="0" cellpadding="0" width="100%">
                                <tr>
                                  <td>Subtotal:</td>
                                  <td><b> $160.00</b></td>
                                </tr>
                                <tr>
                                  <td>Tax</td>
                                  <td>$8.00</td>
                                </tr>
                                <tr>
                                  <td>Amount Due:</td>
                                  <td><b>$168.00</b></td>
                                </tr>
                                <tr>
                                  <td>Due by:</td>
                                  <td>Feb 4, 2014</td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td style="vertical-align:top;" class="desktop-hide">
                              Thank you for your business. Please contact us with any questions regarding this invoice,<br><br>
                              Awesome Co
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </center> -->
        </td>
      </tr>
      <tr>
        <td style="background-color:#1f1f1f;">
          <center>
            <table border="0" cellpadding="0" cellspacing="0" width="600" class="w320" style="height:100%;color:#ffffff" bgcolor="#1f1f1f" >
              <tr>
                <td align="right" valign="middle" class="mobile-padding" style="font-size:12px;padding:20px; background-color:#1f1f1f; color:#ffffff; text-align:left; ">
                  <a style="color:#ffffff;"  href="#">Contact Us</a>&nbsp;&nbsp;|&nbsp;&nbsp;
                  <a style="color:#ffffff;" href="#">Facebook</a>&nbsp;&nbsp;|&nbsp;&nbsp;
                  <a style="color:#ffffff;" href="#">Twitter</a>&nbsp;&nbsp;|&nbsp;&nbsp;
                  <a style="color:#ffffff;" href="#">Support</a>
                </td>
              </tr>
            </table>
          </center>
        </td>
      </tr>
    </table>

    </td>
  </tr>
</table>
</body>
</html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('rvce.resource.portal@gmail.com', EMAIL_PASSWORD)
        smtp.send_message(mssg)
        smtp.close()
    return None


def get_user_instance_by_email(email_id):
    user = userviewMODELS.users.objects.filter(emailID=email_id).first()
    return user

def get_user_instance_by_id(user_id):
    user = userviewMODELS.users.objects.filter(user_id=user_id).first()
    return user


def get_admin_instance_by_id(adminID):
    admin = userviewMODELS.admins.objects.filter(admin_id=adminID).first()
    return admin


def get_resource_instance_by_id(resourceID):
    resource = userviewMODELS.resources.objects.filter(
        resource_id=resourceID).first()
    return resource

def searchComponent(request):
    return render(request, "searchComponent.html")