from django.shortcuts import redirect, render
from django.http import FileResponse
from django.http import HttpResponseRedirect
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from USERVIEW.models import *
import xlwt
from django.http import HttpResponse
from USERVIEW.models import resources as res


def downloadLogs(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, bottomup=0)
    c.setPageSize(size=(600, 2500))
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = []
    logs = resources.objects.raw('''
    select * from users
    join resource_logbook on users.user_id=resource_logbook.member_id
    join resources on resource_logbook.resource_id=resources.resource_id;
    ''')
    lines.append("*********Log Book entry for Resources*********")
    lines.append("")
    lines.append("")
    for log in logs:
        # lines.append(str(log.user_id))
        lines.append("Name: "+str(log.first_name)+" "+str(log.middle_name) +
                     " "+str(log.last_name)+"("+str(log.USN)+")")
        lines.append("Department: "+str(log.department_name))
        lines.append("College mail-ID: "+str(log.emailID))
        lines.append("")
        lines.append("Resource ID: "+str(log.resource_id))
        lines.append("Resource name: "+str(log.resource_name))
        lines.append("Resource OEM: "+str(log.OEM))
        lines.append("Type: "+(str(log.resource_type)))
        lines.append("Issued on: "+str(log.issue_date))
        lines.append("Returned on: "+str(log.return_date))
        lines.append("----------------------")
        lines.append("")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='resource-log-book.pdf')


def downloadRecentSearchedQuery(request):
    return export_users_xls(request)


def export_users_xls(request):
    rows = None
    resource_list = res.objects.none()  # declaring an empty querysert
    if request.method == 'POST':
        # try:
        #     isAdmin = request.session['isAdmin']
        #     username = request.session['username']
        #     isUser = True
        # except:
        #     pass
        searchedQuery = {}
        resource_list1 = res.objects.none()  # declaring an empty querysert
        if request.POST.get('keywords'):
            keywords_list = request.POST.get('keywords').split(' ')
            searchedQuery['keywords'] = request.POST.get('keywords')
            for keyword in keywords_list:
                resource_list1 = resource_list1 | res.objects.filter(
                    resource_name__icontains=keyword)

        resource_list2 = res.objects.none()  # declaring an empty querysert
        if request.POST.get('resourceID'):
            resourceID = request.POST.get('resourceID')
            searchedQuery['resourceID'] = resourceID
            resource_list2 = resource_list2 | res.objects.filter(
                resource_id__contains=resourceID)

        if not request.POST.get('keywords') or not request.POST.get('resourceID'):
            resource_list = resource_list1 | resource_list2
        else:
            resource_list = resource_list1 & resource_list2
        # if request.POST.get('keywords'):
        #     keywords_list = request.POST.get('keywords').split(' ')
        #     searchedQuery['keywords'] = request.POST.get('keywords')
        #     for keyword in keywords_list:
        #         resource_list = resource_list | res.objects.filter(
        #             resource_name__icontains=keyword)
        # if request.POST.get('resourceID'):
        #     resourceID = request.POST.get('resourceID')
        #     searchedQuery['resourceID'] = resourceID
        #     resource_list = resource_list | res.objects.filter(
        #         resource_id__contains=resourceID)
        # if not request.POST.get('resourceID') and not request.POST.get('keywords'):
        #     print("GGGGGGG")
            # resource_list = res.objects.all()
    print(resource_list)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="research-resource-data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Resource Data')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Resource ID', 'Resource Name',  'OEM', 'Type',
               'Department', 'Unit Cost', 'Qty', 'Date of Purchase']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    rows = resource_list
    print(type(rows))
    font_style = xlwt.XFStyle()
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.resource_id, font_style)
        ws.write(row_num, 1, row.resource_name, font_style)
        ws.write(row_num, 2, row.OEM, font_style)
        ws.write(row_num, 3, row.resource_type, font_style)
        ws.write(row_num, 4, row.department_name, font_style)
        ws.write(row_num, 5, row.unit_cost, font_style)
        ws.write(row_num, 6, row.quantity, font_style)
        ws.write(row_num, 7, row.purchase_date.strftime("%Y-%m-%d"), font_style)

    wb.save(response)

    return response
