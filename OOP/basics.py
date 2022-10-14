"""Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects."""

class Myclass:             # This is class which is blueprint
    x = 5

a = Myclass()              # a is an object, we are instantiating an object here.
print(a.x)

# init method

"""All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person('Chetan',24)
print(p1.name, p1.age)

# self parameter
"""The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name         # instance variable
    mysillyobject.age = age           # instance variable
  def myfunc(abc):                    # instance method
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()


# modify/delete object properties:
p1.age = 40; print(p1.age)
del p1.age
print(p1.age)
print(p1.name)
print(p1)
del p1
print(p1)
# Pass statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class People:
    pass


# class : A bluprint for creating objects of a particular type.
# Methods : Regular functions that are part of class.
# Attributes : Variable that holds data that are part of class
# Object : specific instance of class.
# inheritance : means by which class can inherit properties/capabilities and data from other class.
# composition : means of building complex objects out of other objects.
