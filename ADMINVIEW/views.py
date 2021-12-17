from datetime import date
from django.shortcuts import redirect, render
from USERVIEW import models as userviewMODELS


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
        new_logbook_instance = userviewMODELS.resource_logbook()
        new_logbook_instance.admin_id = admin
        new_logbook_instance.resource_id = resource
        new_logbook_instance.member_id = user
        new_logbook_instance.issue_date = date.today().strftime("%Y-%m-%d")
        new_logbook_instance.save()
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
        resource_logbook_record = userviewMODELS.resource_logbook.objects.get(
            log_id=logID)
        print(resource_logbook_record.log_id)
        resource_logbook_record.return_date = date.today().strftime("%Y-%m-%d")
        resource_logbook_record.save()
    return redirect('borrowed-resources')


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
