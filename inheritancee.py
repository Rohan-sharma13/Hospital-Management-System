class person:
    def __init__(self,fname,lname,age):
        self.firstname=fname
        self.lastname=lname
        self.age=age
    def printdata(self):
      print("Name:",self.firstname,self.lastname,"\nAge :",self.age)
class student(person):
    def __init__(self,):
       