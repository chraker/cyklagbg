from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse

from webapp.models import BikeStation


def home(request):
    data = BikeStation.objects.all()
    return TemplateResponse(request, 'index.html', {'data' : data})