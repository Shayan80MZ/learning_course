from ad import Ad


class BaseAdvertising:
    def __init__(self, id):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def describeMe(self):
        pass

    def getClicks(self):
        return self.__clicks

    def getViews(self):
        return self.__views

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1
