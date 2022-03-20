import os, smtplib
from email.message import EmailMessage
from ast import keyword
from concurrent.futures import thread
# from curses import keyname
from datetime import date
from threading import Thread
from django.shortcuts import redirect, render
from USERVIEW import models as userviewMODELS
from django.contrib import messages
from os import link
from time import sleep
import requests, bs4 , sys
import USERVIEW
from django.forms.models import model_to_dict
from django.db import connection



def issueResource(request):
    adminID = None
    isdmin = False
    try:
        isAdmin = request.session['isAdmin']
        if isAdmin:
            adminID = request.session['uid']

    except:
        return redirect('')
    if request.method == "POST" and isAdmin and request.POST.get('emailID'):
        resource_id = request.POST.get('resourceID')
        user_mail_id = request.POST.get('emailID')
        user = get_user_instance_by_email(user_mail_id)
        if user == None:
            messages.info(request, 'Email ID does not exist!!! Try again')
            return redirect('generic-resources-list-view')
        admin = get_admin_instance_by_id(adminID)
        resource = get_resource_instance_by_id(resource_id)
        # print("res_id", resource_id)
        if resource.quantity >= 1:
            resource.quantity -= 1
            resource.save()
            new_logbook_instance = userviewMODELS.resource_logbook()
            new_logbook_instance.admin_id = admin
            new_logbook_instance.resource_id = resource
            new_logbook_instance.member_id = user
            new_logbook_instance.issue_date = date.today().strftime("%Y-%m-%d")
            new_logbook_instance.save()
            print("*********************")
            threadAddResource = Thread(target=sendIssueConfirmationThroughMail, args=('rvce.resource.portal@gmail.com', user, resource, admin, new_logbook_instance))
            threadAddResource.start()
            print("*********************")
            # sendIssueConfirmationThroughMail('rvce.resource.portal@gmail.com', user, resource, admin, new_logbook_instance)
        else:
            messages.info(request, "Currently not available!!! Try later")
            print("Currently not available!!! Try later")
        return redirect('generic-resources-list-view')
    return redirect('')


def borrowedResources(request): # resources borrowed by all the users across departments
    adminID = None
    isAdmin = False
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        if isAdmin:
            adminID = request.session['uid']
    except:
        return redirect('')
    if isAdmin:
        if request.method == 'POST' and (request.POST.get('keywords') or request.POST.get('resourceID')):
            searchedQuery = {}
            resource_list = userviewMODELS.resources.objects.none()  # declaring an empty queryset
            # logbook_resources = userviewMODELS.resources.objects.raw('''
            #     select * from resource_logbook
            #     inner join resources on resource_logbook.resource_id = resources.resource_id
            #     inner join users on resource_logbook.member_id = users.user_id
            #     where return_date is null;
            #     ''')
            
            if request.POST.get('keywords') and request.POST.get('resourceID'):
                keywords = str(request.POST.get('keywords'))
                resourceID = request.POST.get('resourceID')
                searchedQuery['keywords'] = request.POST.get('keywords')
                searchedQuery['resourceID'] = resourceID
                
                resource_list = userviewMODELS.resources.objects.raw(f'''
                    select * from resource_logbook
                    inner join resources on resource_logbook.resource_id = resources.resource_id
                    inner join users on resource_logbook.member_id = users.user_id
                    where return_date is null AND (users.emailID LIKE "%%{keywords}%%" OR users.first_name LIKE "%%{keywords}%%" OR users.last_name LIKE "%%{keywords}%%" OR users.middle_name LIKE "%%{keywords}%%") AND resources.resource_id={resourceID}
                    ''')
                # print(resource_list, "*************************")
                    # AND (users.emailID LIKE '%''' + keywords + '''%' OR users.first_name LIKE '%''' + keywords + '''%' OR users.last_name LIKE '%''' + keywords + '''%' OR users.middle_name LIKE '%''' + keywords + '''%') AND resources.resource_id=''' + resourceID + '''
            elif request.POST.get('keywords'): # searching for list of keywords in the database
                keywords = str(request.POST.get('keywords'))
                searchedQuery['keywords'] = request.POST.get('keywords')
                
                resource_list = userviewMODELS.resources.objects.raw(f'''
                    select * from resource_logbook
                    inner join resources on resource_logbook.resource_id = resources.resource_id
                    inner join users on resource_logbook.member_id = users.user_id
                    where return_date is null AND (users.emailID LIKE "%%{keywords}%%" OR users.first_name LIKE "%%{keywords}%%" OR users.last_name LIKE "%%{keywords}%%" OR users.middle_name LIKE "%%{keywords}%%")
                    ''')
                print(resource_list, "^^^^^^^^^^^^^^^^^^^^^^^^")
                    # AND (users.emailID LIKE '%''' + keywords + '''%' OR users.first_name LIKE '%''' + keywords + '''%' OR users.last_name LIKE '%''' + keywords + '''%' OR users.middle_name LIKE '%''' + keywords + '''%')

            elif request.POST.get('resourceID'):
                resourceID = request.POST.get('resourceID')
                searchedQuery['resourceID'] = resourceID
                resource_list = userviewMODELS.resources.objects.raw('''
                    select * from resource_logbook
                    inner join resources on resource_logbook.resource_id = resources.resource_id
                    inner join users on resource_logbook.member_id = users.user_id
                    where return_date is null AND resources.resource_id={}
                    '''.format(resourceID))

            filtered_resource_list = resource_list
            print(filtered_resource_list)
            if isAdmin:
                return render(request, "borrowed-resources.html", {"resources": filtered_resource_list, "username": username, "admin": 'YES', "searchedQuery": searchedQuery})
            else:
                return redirect('')

        logbook_resources = userviewMODELS.resources.objects.raw('''
        select * from resource_logbook
        inner join resources on resource_logbook.resource_id = resources.resource_id
        inner join users on resource_logbook.member_id = users.user_id
        where return_date is null;
        ''')
        return render(request, 'borrowed-resources.html', {"resources": logbook_resources, "username": username, "admin": "YES"})
    return redirect('')


def returnResource(request):
    isdmin = False
    try:
        isAdmin = request.session['isAdmin']
    except:
        return redirect('')
    if request.method == "POST" and isAdmin and request.POST.get('logID'):
        logID = request.POST.get('logID')
        resourceID = request.POST.get('resourceID')
        resource_logbook_record = userviewMODELS.resource_logbook.objects.get(
            log_id=logID)
        resource = get_resource_instance_by_id(resourceID)
        resource.quantity += 1
        resource.save()
        print(resource_logbook_record.log_id)
        resource_logbook_record.return_date = date.today().strftime("%Y-%m-%d")
        resource_logbook_record.save()
    return redirect('borrowed-resources')


def webScrapperForAddNewResource(keyword, resource_id):
    sleep(10)
    print("Web scrapping for Resources")
    print('Googling...for r_id=', resource_id)
    res = requests.get('https://google.com/search?q=' + keyword) 

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElems = soup.select('div#main > div > div > div > a')  
    numOpen = min(25, len(linkElems))
    linkCount = 0
    for i in range(numOpen):
        if len(linkElems[i].select('h3'))!=0 and linkCount<5:
            print("*********************************************************************")
            heading = "".join(linkElems[i].select('h3')[0].select('div')[0].strings)
            url = 'http://google.com' + linkElems[i].get("href")
            if url and heading:
                newResourceRelatedLinksInstance = userviewMODELS.resourceRelatedLinks()
                newResourceRelatedLinksInstance.url = url
                newResourceRelatedLinksInstance.heading = heading
                newResourceRelatedLinksInstance.resource_id = get_resource_instance_by_id(resource_id)
                newResourceRelatedLinksInstance.save()
                print(heading)
                print(url)
                linkCount+=1


def addResource(request):
    isdmin = False
    username = None
    try:
        isAdmin = request.session['isAdmin']
        adminID = request.session['uid']
        username = request.session['username']
    except:
        return redirect('')
    if request.method == 'POST' and isAdmin:
        new_resource_instance = userviewMODELS.resources()
        new_resource_instance.resource_name = request.POST.get('resourceName')
        new_resource_instance.OEM = request.POST.get('OEM')
        new_resource_instance.resource_type = request.POST.get('resourceType')
        new_resource_instance.department_name = request.POST.get(
            'resourceDeptName')
        new_resource_instance.unit_cost = request.POST.get('unitCost')
        new_resource_instance.location = request.POST.get('location')
        new_resource_instance.purchase_date = request.POST.get('purchaseDate')
        new_resource_instance.quantity = request.POST.get('quantity')
        try:
            new_resource_instance.image = request.FILES['resImage']
        except:
            pass
        new_resource_instance.about = request.POST.get('about')[0:1000]
        new_resource_instance.admin_id = get_admin_instance_by_id(adminID)
        new_resource_instance.save()
        message = "Resource "+new_resource_instance.resource_name+" added successfully"

        print("*********************")
        threadAddResource = Thread(target=webScrapperForAddNewResource, args=(new_resource_instance.resource_name, new_resource_instance.resource_id))
        threadAddResource.start()
        print("*********************")

        return render(request, 'add-resource.html', {"username": username, "message": message, "admin": "YES"})
    if isAdmin:
        return render(request, 'add-resource.html', {"username": username, "admin": "YES"})
    return redirect('')


def updateResource(request):
    isdmin = False
    username = None
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        adminID = request.session['uid']
        print(username, isAdmin, adminID)
    except:
        return redirect('')

    if request.method == 'POST' and isAdmin and request.POST.get('toUpdatePage'): # loads the web page where you can enter updated values
        resourceID = request.POST.get('resourceID')
        resource_instance = get_resource_instance_by_id(resourceID)
        resource_instance.purchase_date = resource_instance.purchase_date.strftime(
            "%Y-%m-%d")
        resource_instance.image = resource_instance.image.url
        print(resource_instance.image)
        return render(request, 'update-resource.html', {"resource": resource_instance, "username": username, "admin": "YES"})

    if request.method == 'POST' and isAdmin and request.POST.get('toUpdate'): # on submit in the web-page of update-resource, this saves the changes in the database
        resourceID = request.POST.get('resourceID')
        resource_instance = get_resource_instance_by_id(resourceID)
        new_resourceUpdateLogbook_instance = userviewMODELS.resourceUpdateLogbook()
        new_resourceUpdateLogbook_instance.admin_id = get_admin_instance_by_id(adminID)
        new_resourceUpdateLogbook_instance.resource_id = resource_instance

        # Checking if any changes and logging the updated values into resourceUpdateLogbook table in database
        if resource_instance.resource_name != request.POST.get('resourceName'):
            new_resourceUpdateLogbook_instance.resource_name = request.POST.get('resourceName')
            resource_instance.resource_name = request.POST.get('resourceName')

        if resource_instance.OEM != request.POST.get('OEM'):
            new_resourceUpdateLogbook_instance.OEM = request.POST.get('OEM')
            resource_instance.OEM = request.POST.get('OEM')

        if resource_instance.resource_type != request.POST.get('resourceType'):
            new_resourceUpdateLogbook_instance.resource_type = request.POST.get('resourceType')
            resource_instance.resource_type = request.POST.get('resourceType')

        if resource_instance.department_name != request.POST.get('resourceDeptName'):
            new_resourceUpdateLogbook_instance.department_name = request.POST.get('resourceDeptName')
            resource_instance.department_name = request.POST.get('resourceDeptName')
        
        if resource_instance.unit_cost != int(request.POST.get('unitCost')):
            new_resourceUpdateLogbook_instance.unit_cost = request.POST.get('unitCost')
            resource_instance.unit_cost = request.POST.get('unitCost')
        
        if resource_instance.location != request.POST.get('location'):
            new_resourceUpdateLogbook_instance.location = request.POST.get('location')
            resource_instance.location = request.POST.get('location')

        if str(resource_instance.purchase_date) != request.POST.get('purchaseDate'):
            print(request.POST.get('purchaseDate'), type(request.POST.get('purchaseDate')))
            print(str(resource_instance.purchase_date), type(resource_instance.purchase_date))
            new_resourceUpdateLogbook_instance.purchase_date = request.POST.get('purchaseDate')
            resource_instance.purchase_date = request.POST.get('purchaseDate')

        if resource_instance.quantity != int(request.POST.get('quantity')):
            # print(type(request.POST.get('quantity')))
            new_resourceUpdateLogbook_instance.quantity = request.POST.get('quantity')
            resource_instance.quantity = request.POST.get('quantity')

        if resource_instance.about.strip() != request.POST.get('about').strip():
            new_resourceUpdateLogbook_instance.about = request.POST.get('about')
            resource_instance.about = request.POST.get('about')
        
        # resource_instance.resource_name = request.POST.get('resourceName')
        # resource_instance.OEM = request.POST.get('OEM')
        # resource_instance.resource_type = request.POST.get('resourceType')
        # resource_instance.department_name = request.POST.get(
        #     'resourceDeptName')
        # resource_instance.unit_cost = request.POST.get('unitCost')
        # resource_instance.location = request.POST.get('location')
        # resource_instance.purchase_date = request.POST.get(
        #     'purchaseDate')
        # resource_instance.quantity = request.POST.get('quantity')
        # # resource_instance.image = request.FILES['resImage']
        # resource_instance.about = request.POST.get('about')
        resource_instance.save()
        new_resourceUpdateLogbook_instance.save()
        message = "Resource "+resource_instance.resource_name+" updated successfully"
        return redirect('generic-resources-list-view')
    return redirect('')


def resourceHistory(request):
    adminID = None
    isAdmin = False
    try:
        isAdmin = request.session['isAdmin']
        username = request.session['username']
        if isAdmin:
            adminID = request.session['uid']
    except:
        return redirect('')
    if isAdmin and request.method == "POST" and request.POST.get('resourceID'):
        resourceID = request.POST.get('resourceID')
        updated_resources_table = userviewMODELS.resources.objects.raw('''
        select * from resourceUpdateLogbook
        inner join admins on admins.user_id = resourceUpdateLogbook.admin_id
        where resourceUpdateLogbook.resource_id = %s
        '''%resourceID)
        # print(updated_resources_table[0].name)
        # print(model_to_dict(updated_resources_table[2]))
        # print(list(updated_resources_table))
        # data = None
        # with connection.cursor() as cursor:
        #     cursor.execute('''
        # select * from resourceUpdateLogbook
        # inner join admins on admins.user_id = resourceUpdateLogbook.admin_id
        # where resourceUpdateLogbook.resource_id = %s
        # '''%resourceID)
        #     data = dictfetchall(cursor)
        #     # print(cursor.description)
        #     # print(data)
        #     # print(len(data))
        #     # print(cursor)
        #     columns = [col[0] for col in cursor.description]
        #     print(columns)
        return render(request, "resource-history-page.html", {"updatedResourceTable": updated_resources_table, "username": username, "admin": "YES"})
    return redirect('')


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



def sendIssueConfirmationThroughMail(From, user, resource, admin, new_logbook_instance):
    sleep(1)
    print("INSIDE THE thread")
    EMAIL_PASSWORD = 'Research@rvce'
    # print("EMAIL_PASSWORD", EMAIL_PASSWORD)
    Subject = f'Resource issued confirmation (Issue ID: {str(new_logbook_instance.log_id)})'
    mssg = EmailMessage()
    mssg['Subject'] = Subject
    mssg['From'] = From
    mssg['To'] = user.emailID
    mssg.set_content("This is the confirmation mail corresponding to the borrowed resource")
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
                    Issued to: <b>""" + user.first_name + " " + user.middle_name + " " + user.last_name +"""</b><br>
                    Issued by: <b>""" + admin.first_name + " " + admin.last_name +"""(System admin)</b><br>
                    Issue date: <b>""" + str(new_logbook_instance.issue_date) + """</b><br>
                    Email-id: """ + user.emailID + """
                    <br>
                    
                    <br>
                    <strong>***Resource details***</strong><br>
                    Resource ID: <strong>""" + str(resource.resource_id) +  """</strong><br>
                    
                    Resource name: <strong>""" + resource.resource_name + """</strong><br>

                    Resource OEM: <strong>""" + resource.OEM + """</strong><br><br><br>

                    <strong>About the Resource: </strong>""" + resource.about + """<br><br><br>

                    <strong>NOTE:</strong> Kindly return it after the use to: <strong>""" + resource.location + ", " + resource.department_name + """</strong><br>
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
                              <a href="location.href='http://127.0.0.1:8000/user-profile/'"
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


def get_admin_instance_by_id(adminID):
    admin = userviewMODELS.admins.objects.filter(user_id=adminID).first()
    return admin


def get_resource_instance_by_id(resourceID):
    resource = userviewMODELS.resources.objects.filter(
        resource_id=resourceID).first()
    return resource


# def returnRecentQuery():
#     return recentSearchedQuery
