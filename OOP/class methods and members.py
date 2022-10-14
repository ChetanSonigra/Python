# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES


    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not as valid book type.')
        else:
            self.booktype = booktype

# TODO: access the class attribute
print(Book.BOOK_TYPES)
print(Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", 'HARDCOVER')
b2 = Book("Title 2", 'PAPERBACK')

# TODO: Use the static method to access a singleton object
# there are not many use cases for static method, one use case is in singleton design pattern. 
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
print(Book.getbooklist())


# class variable in class namespace 
# instance variable in instance/object namespace
class Car:
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()
c2.com = 'Tesla'         # instance variable can be modified by object 
print(c1.mil,c2.com,c1.wheels)     # instance variable can be accessed by object
c1.wheels = 5
print(c1.wheels,c2.wheels, c1.__class__.wheels)
Car.wheels = 6
print(c1.wheels,c2.wheels,c1.__class__.wheels)
# major difference between class variable and instance variable.
# cls var can be accessed by object as well as class, while instance var can only be accessed by object.
# cls var - if modified by class, it affects each instance. if modified by object, then affects only that specific object.

    
