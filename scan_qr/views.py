import json
import requests

from django.shortcuts import render

from django.http import HttpResponse
from scan_qr.models import Eleve

# Create your views here.
def home(request):

    va = Eleve.objects.get(id=1)

    print(va.nom)

    #f = open('C:/Users/T460/Desktop/django/api.json')


    return render(request, 'home.html', {"va": va})

    '''url='https://kinsta.com/wp-json'
    data=requests.get(url).json()'''

def index(request):
    return render(request, 'index.html')

def page1(request):
    return render(request, 'page1.html')

def espace_eleve(request):
    response=requests.get('https://ckhalil.github.io/api/api.json').json()
    return render(request, 'espace_eleve.html',{'response':response})




