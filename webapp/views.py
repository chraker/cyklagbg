import json

import googlemaps as googlemaps
import requests
from django.http import HttpResponse
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

def findcloseststation(request):
    if request.method == 'GET':
        gmaps = googlemaps.Client(key='AIzaSyBQfrwOpfALBdSp12oZcE5dVainE8cI3lk')
        # user_lcoation = gmaps.reverse_geocode(request.GET['location'])[0]["formatted_address"]

        if "geo_location" in request.GET:
            geo_loc = request.GET['geo_location']
            if geo_loc is not None and geo_loc != '':
                user_location =  geo_loc
            else:
                return()
        elif "location" in request.GET:
            loc = request.GET['location']
            if loc is not None and loc != '':
                t_loc = gmaps.geocode(loc)[0]["geometry"]["location"]
                user_location = str(t_loc["lat"]) + "," + str(t_loc["lng"])
            else:
                return()
        else:
            return()

        stations = BikeStation.objects.all()

        c = 0 # temp to save quota
        #find closest
        result = dict()
        result["duration"] = 100000000
        result["from"] = user_location
        for station in stations :
            c+=1
            if c == 10:
                break
            temp_location = ( str(station.long) + "," + str(station.lat) )
            temp_directions = gmaps.distance_matrix(temp_location, user_location) # will probly use up quota fast...
            temp_duration = temp_directions['rows'][0]['elements'][0]['duration']['value']
            if temp_duration < result["duration"]:
                result["duration"] = temp_duration
                result["location"] = temp_location
                result["bikes"] = station.available_bikes

        return HttpResponse(json.dumps(result), content_type='application/json')