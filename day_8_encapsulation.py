class Person:
  def __init__(self, name, age=0):
    self._name = name
    self._age = age

  def display(self):
    print(self._name)
    print(self._age)
a=input("Enter your name:")
b=int(input("Enter your Age:"))
person = Person(a,b)
person.display()
print(person._name)
print(person._age)