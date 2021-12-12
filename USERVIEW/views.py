from django.shortcuts import render
from USERVIEW.models import resources as res


def resources(request):
    # r = res()
    # r.resource_id = 2
    # r.about = "dddd"
    # r.department_name = "ISe"
    # r.resource_name = "Arduino"
    # r.resource_type = "SO"
    # r.location = "Room 120 si"
    # r.purchase_date = "2020-11-12"
    # r.image = "D:\Projects\RESEARCH_RESOURCE_PORTAL\templates\images\blog\blog-01.jpg"
    # r.quantity = 1
    # r.unit_cost = 0
    # r.OEM = "HPE"
    # r.adminId = "ergh3reu3r"
    # r.save()
    resource_list = res.objects.all()
    print("*************", resource_list)

    return render(request, "books-media-list-view.html", {"resources": resource_list})
