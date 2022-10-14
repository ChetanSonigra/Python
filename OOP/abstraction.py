# only shows necessary features, hides implementation details.
# abstract class gives abstract idea about class, 
# We can not instantiate object from abstract class. 
# We can create subclass from abstract class which will have concrete implementation.
# interface shows abilities 
# abstract methods: method that has a declaraction, but does not have implementation
# concrete method: has declaration as well as implementation.

from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcarea(self):
        pass
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calcarea(self):
        return 3.14*(self.radius**2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calcarea(self):
        return self.side**2

# obj = Shape()   throws error 
c1 = Circle(5)          # throws error if calcarea is not defined.
s1 = Square(5)
print(c1.calcarea())
print(s1.calcarea())


# interfaces:
# it promises to provide certain kind of behaviour/ability

class Jsonify(ABC):
    @abstractmethod
    def tojson(self):
        pass
    
class Square(Shape,Jsonify):
    def __init__(self, side):
        self.side = side
    def calcarea(self):
        return self.side**2
    def tojson(self):
        return f"{{ 'Square' : {self.calcarea()}  }}"
    

s1= Square(5)            # throws error if tojson is not defined.
print(s1.tojson()) 