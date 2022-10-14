from dataclasses import dataclass,field
import random

def price_func():
    return float(random.randrange(20,30))
@dataclass
class Book:
    title : str = "No Title"
    author : str = field(default="No Author")                 # 2nd way to provide default value.
    pages : int = 0                                           # way to provide default value
    price : float = field(default_factory=price_func)         # 3rd way to provide default value 

    # __post_init__ function lets us customize additional properties
    # after built in __init__ function finished running.
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}"

b1 = Book()
b2 = Book('C','D',445, 30)
b3 = Book('A','B',1225,44.0)
print(b1.author,b2.pages)
print(b1.description)
print(b1)
# dataclass implements repr and eq magic methods by default.
print(b1)
print(b1==b2)
print(b1==b3)

# change some fields.
print(b3)
b3.title = "aaa"; print(b3)

# create immutable dataclasses, frozen parameter makes class immutable.
@dataclass(frozen=True)
class Immutableclass:
    val1: str = "Value 1"
    val2: int = 0
    def setval1(self,newval):
        self.val1 = newval
obj = Immutableclass()
print(obj.val1)
obj.val1 = "ds"     # throws frozen instance error
obj.setval1("sd")   # throws frozen instance error