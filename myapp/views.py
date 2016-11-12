from django.http import HttpResponse
from django.shortcuts import render
import nmap
from myapp.models import Object
from django.utils import timezone

def home(request):

    o = Object(mac_address='74:2F:68:19:85:70', date_time=timezone.now())
    o.save()

    objects = Object.objects.all()

    return render(request, 'myapp/index.html', {'objects' : objects})
