# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# parent/base class , child/derived class

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

x = Person("Chetan", "Sonigra")
x.printname()

class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)          # or Person.__init__(self, fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear,x.fname)
x.welcome()


# multilevel inheritance
class A:
    def __init__(self):
        self.a = 5
        print(f"object{self} of class A instantiated.")

class B(A):
    def __init__(self):
        self.b = 6
        super().__init__()
        print(f"object {self} of class B instantiated.")

class C(B):
    def __init__(self):
        self.c = 7
        super().__init__()
        print(f"object {self} of class C instantiated.")

a = A()
b = B()
c = C()
print(a.a, b.a, b.b, c.a, c.b, c.c)


# Multiple inheritance:

class A:
    def __init__(self):
        self.a = 5
class B:
    def __init__(self):
        self.b = 6
class C(A,B):
    pass

a = A()
b = B()
c = C()
print(c.a, c.b) # c object has no attribute b, because it follows MRO(method resolution order)
print(C.mro(), C.__mro__)

# MRO:
"""In Python, every class whether built-in or user-defined is derived from the object class and all the objects are instances of the class object. 
Hence, the object class is the base class for all the other classes.
In the case of multiple inheritance, a given attribute is first searched in the current class if it’s not found then it’s searched in the parent classes. 
The parent classes are searched in a left-right fashion and each class is searched once."""

class Class1:
    def m(self):
        print("In Class1")
 
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
 
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
 
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")  
        super().m()
      
obj = Class4()
obj.m()