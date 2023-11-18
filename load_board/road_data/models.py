from django.db import models
from django.utils.translation import gettext_lazy as _
from .enumtype import Preference
# Create your models here.
class Truck(models.Model):
    seq = models.IntegerField()
    truckId = models.IntegerField()
    timeStamp = models.DateTimeField()
    posLatitude = models.FloatField()
    posLongitude = models.FloatField()
    eqType = models.CharField(max_length=100)
    nextTripPref= models.CharField(max_length=2, choices=Preference.choices)
    lastnotified = models.DateTimeField()
    idleTime = models.IntegerField()

class Load(models.Model):
    seq = models.IntegerField()
    timeStamp = models.DateTimeField()
    loadId = models.IntegerField()
    ogLatitude = models.FloatField()
    ogLongtitude = models.FloatField()
    destLatitude = models.FloatField()
    destLongitude = models.FloatField()
    eqType = models.CharField(max_length=100)
    price = models.FloatField()
    mileage = models.FloatField()
    PRICE = 1.18

    def distanceToLoad(self,truckObj):
        distanceToLoad = ((self.ogLatitude-truckObj.posLatitude)**2 + (self.ogLongtitude - truckObj.posLongitude)**2)**(1/2)
        return distanceToLoad
    
    def profitForTruck(self, truckObj):
        profit = self.price
        profit -= self.distanceToLoad(truckObj)*Load.PRICE
        profit -= self.mileage*Load.PRICE
        return profit