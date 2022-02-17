from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
        return render(request, 'toonifyApp/index.html')

def api_toonify(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)



        #TODO TOONIFY HERE



        return HttpResponse(uploaded_file_url)
    else:
        return HttpResponse("Invalid call")
