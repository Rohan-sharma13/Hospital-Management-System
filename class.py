class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
a=input("Enter your name:")
b=int(input("Enter your age:"))
obj=person(a,b)
print("Name :",obj.name)
print("Age :",obj.age)
