from django.shortcuts import render
import json
from django.http import JsonResponse
from . import mqtt_client
# from .models import Truck,Load
import datetime as dt

def read_message(request):
    return "Hello world"

# def publish_message(request):
#     request_data = json.loads(request.body)
#     # to fix the duplicate messages
#     rc, mid = mqtt_client.client.publish(request_data['topic'], request_data['msg'])



# def createRow(jsonObj):
#         jsonObj = jsonObj.decode('UTF-8')
#         jsonObj = json.loads(jsonObj)
#         if jsonObj['type'] == 'Truck':
#             loadDetails = jsonObj
#             seq = loadDetails['seq']
#             timeStamp = loadDetails['timeStamp']
#             loadId = loadDetails['loadId']
#             ogLatitude = loadDetails['originLatitude']
#             ogLongitude = loadDetails['originLongtitude']
#             destLatitude = loadDetails['destinationLatitude']
#             destLongitude = loadDetails['destinationLongtitude']
#             eqType = loadDetails['equipmentType']
#             price = loadDetails['price']
#             mileage = loadDetails['mileage']
#             load = Load(seq = seq, timeStamp = timeStamp, loadId = loadId, ogLatitude = ogLatitude, ogLongitude = ogLongitude, 
#                         destLatitude = destLatitude, destLongitude = destLongitude, eqType = eqType, price = price, mileage = mileage)
#             load.save()
#         elif jsonObj['type'] == 'Load':
#             truckDetails = jsonObj
#             seq = truckDetails['seq']
#             timeStamp = truckDetails['timestamp']
#             truckId = truckDetails['truckId']
#             posLatitude = truckDetails['positionLatitude']
#             posLongitude = truckDetails['positionLongtitude']
#             eqType = truckDetails['equipType']
#             nextTripPref = truckDetails['nextTripLengthPreference']
#             truck = Truck(seq = seq,timeStamp=timeStamp,truckId = truckId,posLatitude = posLatitude, posLongitude = posLongitude,
#                         eqType = eqType, nextTripPref = nextTripPref, idleTime = 0, lastnotified=dt.datetime.now())
#             truck.save()