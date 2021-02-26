from base_model import BaseAdvertising


class Ad(BaseAdvertising):
    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self):
        return self.__imgUrl

    def setImgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link

    def setAdvertiser(self, advertiser):
        self.__advertiser = advertiser

    def describeMe(self):
        return "This class is used for ads"
