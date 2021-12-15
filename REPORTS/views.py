from django.shortcuts import render

# Create your views here.
from django.http import FileResponse
from django.http import HttpResponseRedirect
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from USERVIEW.models import *


def venue_pdf(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3",
    # ]
    
    lines = []
    venues=resources.objects.all()


    for venue in venues:
        lines.append(str(venue.resource_id))
        lines.append(str(venue.resource_name))
        lines.append(str(venue.OEM))
        lines.append(str(venue.resource_type))
        lines.append(str(venue.department_name))
        lines.append(str(venue.unit_cost))
        lines.append("=========================")
    
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')