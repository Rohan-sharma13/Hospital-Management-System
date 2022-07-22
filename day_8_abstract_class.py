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
    def __init__(self, taste="Sweet",color="yellow"):
        self.shape = "Oval"
        self.taste = taste
        self.color = color

    def getshape(self):
        return self.shape

    def getcolor(self):
        return self.color

    def gettaste(self):
        return self.taste


normal_mango = Mango()
wild_mango = Mango("Sour","green")
print("Taste of  mango:",normal_mango.gettaste())
print("Shape of mango:",normal_mango.getshape())
print("color of  mango:",normal_mango.getcolor())
print("Taste of Wild mango:",wild_mango.gettaste())
print("Shape of wild mango:",wild_mango.getshape())
print("color of wild mango:",wild_mango.getcolor())
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
print("Taste of orange:",my_orange.gettaste())
print("Shape of orange:",my_orange.getshape())
print("color of orange:",my_orange.getcolor())
