# customize object behaviour and integrate with langauge.
# define how objects are represented as string.
# control access to attribute values, both for get and set.
# build in comparision, equality testing capabilities.

# __add__, __eq__, __lt__, __gt__

# Attribute access: __getattribute__, __setattr__, __getattr__
class Book:
    def __init__(self,title,author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1
    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"
    def __getattribute__(self,name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return (p-(p*d))
        return super().__getattribute__(name)
    def __setattr__(self,name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be float")
        return super().__setattr__(name,value)  
    def __getattr__(self,name):          
        # only gets called when __getattribute__ doesnot exist or it throws exception 
        #  or attribute does not exist.
        # we can generate attribute on the fly.
        return name + " is not here!" 
    def __str__(self):
        return f" {self.title} : {self.price} "
    def __call__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def __contains__(self,something):
        return something.lower() in self.title.lower()
    
    def __enter__(self):
        self.open = True
        self._discount = 0.5

    def __exit__(self, exc_type, exc_value, traceback):
        self._discount = 0.1
        self.open = False

    def __del__(self):
        print(f"{self.title} is deleted.")

b1 = Book('ABC','Auth',40.0)
b2 = Book('ABC2','Auth2',50.0)
print(b1.price,b1)
b1.price = 50.0
print(b1.price,b1)
print(b1.raflk)
print('ABC' in b1)

# callable object: __call__ function override
print(b1)
b1('A',"B",50.0)
print(b1)

del b2


print(b1.price, b1.open)

with b1 as b:
    print(b1.price, b1.open)

print(b1.price, b1.open)

# __enter__ , __exit__ for deciding actions in with statement.
# __setitem__, __getitem__ for indexing and item assignment.
# __del__ destructor.
# __iter__ , __next__ for iterating over objects
# __contains__ to check if item is present in object.



