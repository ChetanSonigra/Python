
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '4 GB'


s1 = Student('chetan',1)
s2 = Student('RAM',2)
s1.show()
s2.show()
print(id(s1.lap),id(s2.lap))
lap1 = Student.Laptop()        # CAN'T create directly, have to call inside outer class
