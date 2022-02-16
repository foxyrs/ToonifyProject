from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'param': "YaY"
    }
    return render(request, 'toonifyApp/index.html', context)
