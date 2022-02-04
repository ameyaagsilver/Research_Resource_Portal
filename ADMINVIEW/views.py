from concurrent.futures import thread
from datetime import date
from threading import Thread
from django.shortcuts import redirect, render
from USERVIEW import models as userviewMODELS
from django.contrib import messages
from os import link
from time import sleep
import requests, bs4 , sys

import USERVIEW

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
        print("res_id", resource_id)
        if resource.quantity >= 1:
            resource.quantity -= 1
            resource.save()
            new_logbook_instance = userviewMODELS.resource_logbook()
            new_logbook_instance.admin_id = admin
            new_logbook_instance.resource_id = resource
            new_logbook_instance.member_id = user
            new_logbook_instance.issue_date = date.today().strftime("%Y-%m-%d")
            new_logbook_instance.save()
        else:
            print("Currently not available!!! Try later")
        return redirect('generic-resources-list-view')
    return redirect('')


def borrowedResources(request):
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

        logbook_resources = userviewMODELS.resources.objects.raw('''
        select * from resource_logbook
        inner join resources on resource_logbook.resource_id = resources.resource_id
        inner join users on resource_logbook.member_id = users.user_id
        where return_date is null;
        ''')
        # global recentSearchedQuery
        # recentSearchedQuery = logbook_resources
        # print(logbook_resources)
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

        if resource_instance.purchase_date != request.POST.get('purchaseDate'):
            new_resourceUpdateLogbook_instance.purchase_date = request.POST.get('purchaseDate')
            resource_instance.purchase_date = request.POST.get('purchaseDate')

        if resource_instance.quantity != int(request.POST.get('quantity')):
            # print(type(request.POST.get('quantity')))
            new_resourceUpdateLogbook_instance.quantity = request.POST.get('quantity')
            resource_instance.quantity = request.POST.get('quantity')

        if resource_instance.about != request.POST.get('about'):
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
