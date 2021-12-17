from django.shortcuts import redirect, render
from .models import resources as res


def resources(request):  # DISPLAYs all resources a user taken resources
    try:
        user_id = request.session['uid']
        username = request.session['username']
        isAdmin = request.session['isAdmin']
        print(isAdmin, user_id, username)
        resource_list = res.objects.raw('''select * from users 
                                    join resource_logbook on users.user_id=resource_logbook.member_id
                                    join resources on resource_logbook.resource_id=resources.resource_id
                                    where users.user_id="%s"
                                    ''' % user_id)
        print("User Borrowed resources are", resource_list)
        if isAdmin:
            return render(request, "USERVIEW/userResources.html", {"resources": resource_list, "username": username, "admin": 'YES'})
        return render(request, "USERVIEW/userResources.html", {"resources": resource_list, "username": username})
    except:
        pass

    return render(request, "USERVIEW/userResources.html")


# searches for resource searched w.r.t a keyword or the resourceID provided
# def searchResources(request):
#     isAdmin = False
#     resource_list = res.objects.none()  # declaring an empty querysert
#     if request.method == 'POST':
#         try:
#             isAdmin = request.session['isAdmin']
#             username = request.session['username']
#         except:
#             pass
#         if request.POST.get('keywords'):
#             keywords_list = request.POST.get('keywords').split(' ')

#             for keyword in keywords_list:
#                 resource_list = resource_list | res.objects.filter(
#                     resource_name__icontains=keyword)
#         if request.POST.get('resourceID'):
#             resourceID = request.POST.get('resourceID')
#             resource_list = resource_list | res.objects.filter(
#                 resource_id__contains=resourceID)
#         print(resource_list)
#         if isAdmin:
#             return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username, "admin": 'YES'})
#         return render(request, "generic-resources-list-view.html", {"resources": resource_list, "username": username})

#     return render(request, "generic-resources-list-view.html")
