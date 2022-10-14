"""Both str() and repr() methods are used for the string representation of an object. 
The difference between str() and repr() is that str() returns a user-friendly version
of an object. The repr() method returns a developer-friendly string representation of an object."""

import datetime
from unicodedata import name
today = datetime.datetime.now()
print(str(today))   # calls __str__ method
print(repr(today))  # calls __repr__ method
print(today)  

# when you call print() on an object, it calls __str__ method of the object. If __str__ is not implemented, the __repr__ is called as a fallback.

# we can modify these methods for user defined class.

# If we don't provide str/repr method, it will show by default representation of object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} - {self.age}"
    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.name})"    

p1 = Person('chetan',23)
print(p1)                   # <__main__.Person object at 0x000001D53348F550> -- default when no str or repr method is defined.

# Person(chetan)  --> when there is only repr defined, not str
# chetan - 23 --> when both str and repr is defined.