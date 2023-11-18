from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Truck,Load
import datetime as dt

@csrf_exempt
def read_message(request):
    if request.method == 'POST':
        jsonObj = request.body.decode('UTF-8')
        jsonObj = json.loads(jsonObj)
        createRow(jsonObj)
    return HttpResponse("You good bro")

# def publish_message(request):
#     request_data = json.loads(request.body)
#     # to fix the duplicate messages
#     rc, mid = mqtt_client.client.publish(request_data['topic'], request_data['msg'])

def see_dataTruck(request):
    return HttpResponse(Truck.objects.all())

def see_dataLoad(request):
    return HttpResponse(Load.objects.all())


def createRow(jsonObj):
    if jsonObj['type'] == 'Load':
        loadDetails = jsonObj
        seq = loadDetails['seq']
        timeStamp = loadDetails['timestamp']
        loadId = loadDetails['loadId']
        ogLatitude = loadDetails['originLatitude']
        ogLongitude = loadDetails['originLongitude']
        destLatitude = loadDetails['destinationLatitude']
        destLongitude = loadDetails['destinationLongitude']
        eqType = loadDetails['equipmentType']
        price = loadDetails['price']
        mileage = loadDetails['mileage']
        load = Load(seq = seq, timeStamp = timeStamp, loadId = loadId, ogLatitude = ogLatitude, ogLongitude = ogLongitude, 
                    destLatitude = destLatitude, destLongitude = destLongitude, eqType = eqType, price = price, mileage = mileage)
        load.save()
        print("Wrote succesfully")
    elif jsonObj['type'] == 'Truck':
        truckDetails = jsonObj
        seq = truckDetails['seq']
        timeStamp = truckDetails['timestamp']
        truckId = truckDetails['truckId']
        posLatitude = truckDetails['positionLatitude']
        posLongitude = truckDetails['positionLongitude']
        eqType = truckDetails['equipType']
        nextTripPref = truckDetails['nextTripLengthPreference']
        truck = Truck(seq = seq,timeStamp=timeStamp,truckId = truckId,posLatitude = posLatitude, posLongitude = posLongitude,
                    eqType = eqType, nextTripPref = nextTripPref, idleTime = 0, lastnotified=dt.datetime.now())
        truck.save()
        print("Wrote succesfully")