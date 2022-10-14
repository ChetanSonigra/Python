# it is to represent one thing in many form.
# 1. duck typing  2. operator overloading  3. method overloading 4. method overriding

# 1. duck typing : it it acts like a duck, quacks like a duck then it is a duck.
x =5             # there is a object of 5 and we are naming it as x.
x = 'Chetan'     # there is a object of 'Chetan' and we are naming it as x

class Pycharm():
    def execute(self):
        print("compiling")
        print("running")
class MyEditor():
    def execute(self):
        print('spell check')
        print('compiling')
        print('running')
class Laptop:
    def code(self,ide):          # we can give any object as ide who has execute method.
        ide.execute()
ide =Pycharm()
ide2 = MyEditor()
lap1 =Laptop()
lap1.code(ide)
lap1.code(ide2)


# 2. Operator Overloading:
# using operators for different type of objects.

a = 5; b = 14
print(a + b)
print(int.__add__(a,b))
a = 'd' ; b = 't'
print(a+b); print(str.__add__(a,b))
# __add__, __gte__, __lte__, __sub__, __mul__

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1+ other.m1
        m2 = self.m2 +other.m2
        return Student(m1/2,m2/2)
s1 = Student(55,33)
s2 = Student(44,66)
s3 = s1 + s2
print(s3.m1,s3.m2)

# method overloading :
#  it is not there in python. in a class if  you have method with same name with different arguments.
# we can use *args , **kwargs for variable arguments. this is possible by providing default arguments as well.

# method overriding : in subclass, we can override the method from it's base class.
class A:
    def __init__(self):
        pass
    def show(self):
        return "in A show"

class B(A):
    def __init__(self):
        super().__init__()
    def show(self):
        return "in B show"

b = B()
b.show()
