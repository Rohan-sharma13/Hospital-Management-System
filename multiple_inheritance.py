class Father():
    def Driving(self):
        print("Father Enjoys Driving")
class Mother():
    def Cooking(self):
        print("Mother Enjoys Cooking")
class Child(Father, Mother):
    def Playing(self):
        print("Child Loves Playing")
c = Child()
c.Driving()
c.Cooking()
c.Playing()