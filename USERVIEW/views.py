from django.shortcuts import redirect, render
from .models import resources as res


def resources(request):  # DISPLAYs all a user taken resources

    try:
        user_id = request.session['uid']
        username = request.session['username']
        resource_list = res.objects.raw('''select * from users 
                                    join resource_logbook on users.user_id=resource_logbook.member_id_id
                                    join resources on resource_logbook.resource_id_id=resources.resource_id
                                    where users.user_id="%s"
                                    ''' % user_id)
        print("((((",resource_list)
        return render(request, "USERVIEW/userResources.html", {"resources": resource_list, "username":username})
    except:
        pass

    return render(request, "USERVIEW/userResources.html")
