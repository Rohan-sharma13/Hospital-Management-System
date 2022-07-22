class Person:
  def __init__(self, name, age=0):
    self.__name = name
    self.__age = age

  def display(self):
    print(self.__name)
    print(self.__age)
a=input("Enter your name:")
b=int(input("Enter your Age:"))
person = Person(a,b)
person.display()
print('Trying to access variables from outside the class ')
print(person.__name)
print(person.__age)