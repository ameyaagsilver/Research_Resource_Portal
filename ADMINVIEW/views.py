from datetime import date
from django.shortcuts import redirect, render
from USERVIEW import models as userviewMODELS

# recentSearchedQuery = None


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
        new_resource_instance.image = request.FILES['resImage']
        new_resource_instance.about = request.POST.get('about')
        new_resource_instance.admin_id = get_admin_instance_by_id(adminID)
        new_resource_instance.save()
        message = "Resource "+new_resource_instance.resource_name+" added successfully"
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
    except:
        return redirect('')

    if request.method == 'POST' and isAdmin and request.POST.get('toUpdatePage'):
        resourceID = request.POST.get('resourceID')
        resource_instance = get_resource_instance_by_id(resourceID)
        resource_instance.purchase_date = resource_instance.purchase_date.strftime(
            "%Y-%m-%d")
        resource_instance.image = resource_instance.image.url
        print(resource_instance.image)
        return render(request, 'update-resource.html', {"resource": resource_instance, "username": username, "admin": "YES"})

    if request.method == 'POST' and isAdmin and request.POST.get('toUpdate'):
        resourceID = request.POST.get('resourceID')
        resource_instance = get_resource_instance_by_id(resourceID)
        resource_instance.resource_name = request.POST.get('resourceName')
        resource_instance.OEM = request.POST.get('OEM')
        resource_instance.resource_type = request.POST.get('resourceType')
        resource_instance.department_name = request.POST.get(
            'resourceDeptName')
        resource_instance.unit_cost = request.POST.get('unitCost')
        resource_instance.location = request.POST.get('location')
        resource_instance.purchase_date = request.POST.get(
            'purchaseDate')
        resource_instance.quantity = request.POST.get('quantity')
        # resource_instance.image = request.FILES['resImage']
        resource_instance.about = request.POST.get('about')
        resource_instance.save()

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


def returnRecentQuery():
    return recentSearchedQuery
