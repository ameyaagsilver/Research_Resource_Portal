from django.shortcuts import render
from .models import emp

def insertRecord(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('country') and request.POST.get('emailID'):
            record = emp()
            record.country = request.POST.get('country')
            record.emailID = request.POST.get('emailID')
            record.name = request.POST.get('name')
            record.save()
            messages = "Record inserted successfully..."

            return render(request, 'testDB/index.html', {'mssg':messages})
    return render(request, 'testDB/index.html')