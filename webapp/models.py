from django.db import models

# Model for a station
class BikeStation(models.Model):
    name = models.CharField(max_length=100)
    available_bike_stands = models.IntegerField()
    available_bikes = models.IntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    isopen = models.BooleanField()

