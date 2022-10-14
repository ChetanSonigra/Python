# 1. single _ in interpreter.
# it gives last executed expression
# 2. single _ for ignoring values.
for _ in range(10):       # ignore value of index/location.
    print("test")

# a,b,_,_ = my_method(var1) # ignore a value when unpacking 

# 3. single _ after name to differentiate variable from keyword.
class_ = 8

# 4. single _ in numeric literals
# grouping decimal for easy readability of long literals
amount = 10_000_000.0
print(amount)
# grouping hexadecimal for easy readability of long literals
addr = 0xCAFE_F00D
# grouping bits for easy readability of long literals
flags = 0b_0011_1111_0100_1110

# 5. protected member
class Prefix:
    def __init__(self):
        self.public = 10
        self._protected = 12
        self.__private = 14


class Prefixsubclass(Prefix):
    def getprotected(self):
        return self._protected 
    def getprivate(self):
        self.__private += 5   
        return self.__private

test = Prefix()
print(test.public)
print(test._protected)
# print(test.__private)               throws attribute error
print(test._Prefix__private)          # name mangling in python

test2 = Prefixsubclass()
print(test2.public)
print(test2._protected)         # works
print(test2._Prefix__private)   # name mangling in python       
print(test2.__private)          # throws attribute error
print(test2.getprotected())     # works
print(test2.getprivate())       # does not work can work with name mangling



#  Use of double _
# 1. private member
# 2. magic methods which can be used for operator overloading.

