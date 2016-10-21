from django.http import HttpResponse
from django.shortcuts import render
import nmap
from myapp.models import Person

def home(request):
    persons = Person.objects.all()

    return render(request, 'myapp/index.html', {'persons' : persons})
