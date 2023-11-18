class Trucks():
    def __init__(self,seq,timeStamp,truckId, posLatitude, posLongitude, eqType, nextTripPreference):
        self.seq = seq
        self.timeStamp = timeStamp
        self.truckId = truckId
        self.posLatitude = posLatitude
        self.posLongitude = posLongitude
        self.eqType = eqType
        self.nextTripPreference = nextTripPreference
        self.idleTime = 0