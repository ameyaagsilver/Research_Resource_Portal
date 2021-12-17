from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponseRedirect
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from USERVIEW.models import *


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
    # for venue in venues:
    #     lines.append(str(users.resource_id))
    #     lines.append(str(venue.resource_name))
    #     lines.append(str(venue.OEM))
    #     lines.append(str(venue.resource_type))
    #     lines.append(str(venue.department_name))
    #     lines.append(str(venue.unit_cost))
    #     lines.append("=========================")
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
