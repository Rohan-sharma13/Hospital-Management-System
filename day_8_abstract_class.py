from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):

    @abstractmethod
    def getshape(self):
        print(self.name)

    @abstractmethod
    def getcolor(self):
        return self.color

    @abstractmethod
    def gettaste(self):
        return self.taste


class Mango(Fruit):
    def __init__(self, taste="Sweet"):
        self.shape = "Oval"
        self.taste = taste
        self.color = "Orange"

    def getshape(self):
        return self.shape

    def getcolor(self):
        return self.color

    def gettaste(self):
        return self.taste


normal_mango = Mango()
wild_mango = Mango("Sour")
print(wild_mango.gettaste())


class Orange(Fruit):
    def __init__(self):
        self.taste = "Sweet"
        self.color = "Orange"
        self.shape = "Spherical"

    def getshape(self):
        return self.shape

    def getcolor(self):
        return self.color

    def gettaste(self):
        return self.taste


my_orange = Orange()