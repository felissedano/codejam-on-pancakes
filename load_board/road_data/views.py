from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Trucker, Load
# Create your views here.
def index(request):
    # return render('index.html')
#       "seq": 3,
#   "type": "Load",
#   "timestamp": "2023-11-17T11:31:35.0481646-05:00",
#   "loadId": 101,
#   "originLatitude": 39.531354,
#   "originLongitude": -87.440632,
#   "destinationLatitude": 37.639,
#   "destinationLongitude": -121.0052,
#   "equipmentType": "Van",
#   "price": 3150.0,
# #   "mileage": 2166.0


#     loadid = models.IntegerField()
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     price = models.FloatField()
#     mileage = models.FloatField()
#     type = models.CharField(
#         max_length=2,
#         choices=TruckType.choices
#     )
    # l = Load(loadid=101,latitude=39.531354,longitude=37.639,price=3150.0,mileage=2166.0,type='VN')
    # l.save()

    # template = loader.get_template("polls/index.html")

    return render(request, "index.html")
