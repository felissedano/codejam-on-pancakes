from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Truck,Load, Notification
import datetime as dt

def index(request):
    return render(request, 'index.html')

def credits(request):
    return render(request, 'credits.html')

@csrf_exempt
def read_message(request):
    if request.method == 'POST':
        jsonObj = request.body.decode('UTF-8')
        jsonObj = json.loads(jsonObj)
        createRow(jsonObj)
        return HttpResponse("Mesg recieved successfully!")
    else:
        return HttpResponse("There was some issue")

def create_notif(compatible: dict):
    for k,v in compatible.items():
        for truck in v:
            if truck[1] > 0:
                message = f"Hi {truck[0].truckId}, load {k.loadId} available, and you'll make {truck[1]} money!"
                notification = Notification(truckId=truck[0].truckId, loadId=k.loadId,message=message, timeSent=dt.datetime.now())
                notification.save()

def updateNotifications(request):
    eqType = ['Van','FlatBed','Reefer']
    compatible = {}
    for e in eqType:
        loads = Load.objects.filter(eqType=e)
        trucks = Truck.objects.filter(eqType=e)
        for l in loads:
            compatible[l] = []
            for t in trucks:
                compatible[l].append((t, l.profitForTruck(t)))
    create_notif(compatible)
    return HttpResponse(compatible)

def see_dataTruck(request):
    return HttpResponse(Truck.objects.all())

def see_dataLoad(request):
    return HttpResponse(Load.objects.all())

def see_dataNotif(request):
    context = list(Notification.objects.values())
    context = {'data': context}
    return render(request,'table.html', context)

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