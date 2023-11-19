import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from .enumtype import Preference, EquipmentType
# Create your models here.
class Truck(models.Model):
    seq = models.IntegerField()
    truckId = models.IntegerField(primary_key=True)
    timeStamp = models.DateTimeField()
    posLatitude = models.FloatField()
    posLongitude = models.FloatField()
    eqType = models.CharField(max_length=2, choices=EquipmentType.choices)
    nextTripPref= models.CharField(max_length=2, choices=Preference.choices)
    lastnotified = models.DateTimeField()
    idleTime = models.IntegerField()

    def __str__(self):
        return "truckId: " + str(self.truckId) + ", timestamp: " + str(self.timeStamp) + "equip: " +  self.eqType
    
    def __eq__(self,other):
        return self.truckId == other.truckId

class Load(models.Model):
    seq = models.IntegerField()
    timeStamp = models.DateTimeField()
    loadId = models.IntegerField(primary_key=True)
    ogLatitude = models.FloatField()
    ogLongitude = models.FloatField()
    destLatitude = models.FloatField()
    destLongitude = models.FloatField()
    eqType = models.CharField(max_length=2, choices=EquipmentType.choices)
    price = models.FloatField()
    mileage = models.FloatField()
    PRICE = 1.18

    def __str__(self):
        return "LoadId: " + str(self.loadId) + ", timestamp: " + str(self.timeStamp) + "equip: " +  self.eqType

    def distanceToLoad(self,truckObj):
        distanceToLoad = ((self.ogLatitude-truckObj.posLatitude)**2 + (self.ogLongitude - truckObj.posLongitude)**2)**(1/2)
        return distanceToLoad
    
    def profitForTruck(self, truckObj):
        profit = self.price
        profit -= self.distanceToLoad(truckObj)*Load.PRICE
        profit -= self.mileage*Load.PRICE
        return profit
    
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    truckId = models.IntegerField()
    loadId = models.IntegerField()
    timeSent = models.DateTimeField()
    message = models.CharField(max_length=200)


    def __str__(self):
        return "<p>" + str(self.message) + "at" + str(self.timeSent) + "\n next \n" + "</p>"
