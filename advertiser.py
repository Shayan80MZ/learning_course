from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    allAdvertisers = set()

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name
        Advertiser.allAdvertisers.add(self)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def help(self):
        return dir(self)

    @staticmethod
    def getTotalClicks():
        clicksList = list()
        for advertiser in Advertiser.allAdvertisers:
            clicksList.append(advertiser.getClicks())

        return sum(clicksList)
