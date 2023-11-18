class Load():
    PRICE = 1.18
    def __init__(self, seq, timeStamp, loadId, ogLatitude, ogLongitude, destLatitude, destLongitude, eqType, price, mileage):
        self.seq = seq
        self.timeStamp = timeStamp
        self.loadId = loadId
        self.ogLatitude = ogLatitude
        self.ogLongtitude = ogLongitude
        self.destLatitude = destLatitude
        self.destLongitude = destLongitude
        self.eqType = eqType
        self.price = price
        self.mileage = mileage

    def distanceToLoad(self,truckObj):
        distanceToLoad = ((self.ogLatitude-truckObj.posLatitude)**2 + (self.ogLongtitude - truckObj.posLongitude)**2)**(1/2)
        return distanceToLoad
    
    def profitForTruck(self, truckObj):
        profit = self.price
        profit -= self.distanceToLoad(truckObj)*Load.PRICE
        profit -= self.mileage*Load.PRICE
        return profit