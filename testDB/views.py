from django.shortcuts import render
from USERVIEW.models import test


def insertRecord(request):
    print("hello")
    if request.method == "POST":
        if request.POST.get('name'):
            print("HHHHH")
            record = test()
            record.name = request.POST.get('name')
            print(request.FILES)
            record.image = request.FILES['image']
            print("***", record.save())
            messages = "Record inserted successfully..."

            return render(request, 'testDB/index.html', {'mssg': messages})
    return render(request, 'testDB/index.html')
