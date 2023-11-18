from django.db import models
from django.utils.translation import gettext_lazy as _
from .enumtype import TruckType, Preference
# Create your models here.
class Trucker(models.Model):

    truckerid = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    lastnotified = models.DateTimeField('last notified')
    type = models.CharField(
        max_length=2,
        choices=TruckType.choices
    )
    pref = models.CharField(
        max_length=2,
        choices=Preference.choices
    )
    

class Load(models.Model):
    loadid = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.FloatField()
    mileage = models.FloatField()
    type = models.CharField(
        max_length=2,
        choices=TruckType.choices
    )







        




        