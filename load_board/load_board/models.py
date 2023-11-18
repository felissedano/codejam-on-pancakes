import json
from events.trucks import Trucks
from events.loads import Loads

class Models():
    def __init__(self):
        self.truckers = []
        self.loads = []

    def addTrucker(self,truckDetails):
        seq = truckDetails['seq']
        timeStamp = truckDetails['timestamp']
        truckId = truckDetails['truckId']
        posLatitude = truckDetails['positionLatitude']
        posLongitude = truckDetails['positionLongtitude']
        eqType = truckDetails['equipType']
        nextTripPreference = truckDetails['nextTripLengthPreference']
        truck = Trucks(seq,timeStamp,truckId,posLatitude,posLongitude,eqType,nextTripPreference)
        self.truckers.append(truck)

    def addLoad(self,loadDetails):
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
        load = Loads(seq,timeStamp,loadId,ogLatitude,ogLongitude,destLatitude,destLongitude,eqType,price,mileage)
        self.loads.append(load)

    def instantiateObject(self,jsonObj):
        jsonObj = jsonObj.decode('UTF-8')
        jsonObj = json.loads(jsonObj)
        if jsonObj['type'] == 'Truck':
            self.addTrucker(jsonObj)
        elif jsonObj['type'] == 'Load':
            self.addLoad(jsonObj)