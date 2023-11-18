import json
from models import Truck, Load

def addLoad(loadDetails):
    seq = loadDetails['seq']
    timeStamp = loadDetails['timeStamp']
    loadId = loadDetails['loadId']
    ogLatitude = loadDetails['originLatitude']
    ogLongitude = loadDetails['originLongtitude']
    destLatitude = loadDetails['destinationLatitude']
    destLongitude = loadDetails['destinationLongtitude']
    eqType = loadDetails['equipmentType']
    price = loadDetails['price']
    mileage = loadDetails['mileage']
    load = Load(seq = seq, timeStamp = timeStamp, loadId = loadId, ogLatitude = ogLatitude, ogLongitude = ogLongitude, 
                destLatitude = destLatitude, destLongitude = destLongitude, eqType = eqType, price = price, mileage = mileage)
    load.save()

def addTrucker(truckDetails):
    seq = truckDetails['seq']
    timeStamp = truckDetails['timestamp']
    truckId = truckDetails['truckId']
    posLatitude = truckDetails['positionLatitude']
    posLongitude = truckDetails['positionLongtitude']
    eqType = truckDetails['equipType']
    nextTripPref = truckDetails['nextTripLengthPreference']
    truck = Truck(seq = seq,timeStamp=timeStamp,truckId = truckId,posLatitude = posLatitude, posLongitude = posLongitude,
                  eqType = eqType, nextTrepPref = nextTripPref, idleTime = 0)
    truck.save()

def createRow(jsonObj):
        jsonObj = jsonObj.decode('UTF-8')
        jsonObj = json.loads(jsonObj)
        if jsonObj['type'] == 'Truck':
            addTrucker(jsonObj)
        elif jsonObj['type'] == 'Load':
            addLoad(jsonObj)