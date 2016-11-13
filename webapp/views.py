import json

import requests
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.template.response import TemplateResponse

from webapp.models import BikeStation


def findbike(request):
    data = BikeStation.objects.all()
    return TemplateResponse(request, 'findbike.html', {'data' : data, 'nbar': ''})

def stations(request):
    data = BikeStation.objects.all()
    return TemplateResponse(request, 'stations.html', {'data' : data, 'nbar': 'stations'})

def directions(request):
    data = BikeStation.objects.all()
    return TemplateResponse(request, 'directions.html', {'data' : data, 'nbar': 'directions'})

# def getbike(request):
#     if request.method == 'GET':
#         # get location as long/lat
#         request_str = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCGTxlg3YzIgRVdPD3HFpYlMkrSyxQNHyI"
#         request_str += "&address=" + request.GET['location'].replace(", ","+")
#
#         location = requests.get(request_str).content.decode("utf-8").replace("\n","")
#         location = json.loads(location)
#         loc_data = location["results"][0]["geometry"]["location"]
#         locatior_str = str(loc_data["lat"])+","+ str(loc_data["lng"])
#
#         # make matrix search for bike stations
#         request_str = "https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyCGTxlg3YzIgRVdPD3HFpYlMkrSyxQNHyI"
#         request_str += "&origins=" + locatior_str
#         request_str +="&destiantions="
#         data = BikeStation.objects.all()
#         for station in data:
#             if station.available_bikes > 0 :
#                 request_str += str(station.lat)
#                 request_str += ","
#                 request_str += str(station.long)
#                 request_str += "|"
#
#         request_str += "&mode=walking"
#
#         r = requests.get(request_str)
#
#         # get closest station
#         r.doh