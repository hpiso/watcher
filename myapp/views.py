from django.http import HttpResponse
from django.shortcuts import render
import nmap
from myapp.models import Object

def home(request):
    objects = Object.objects.all()

    return render(request, 'myapp/index.html', {'objects' : objects})
