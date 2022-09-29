# variables are containers for storing data values
# python does not have any command for declaring variable.
# a variable is created when you first assign value to it.
# 3 rules for variable name
# 1. it contains only letters,numbers and _ 
# 2. it should not start with number 
# 3. it is case sensitive.
a = 5
b = "lsdfj"
c = 'hdsifh'
# string values can be in single quote or double quote.

# casting
a = int(4.3)
b = str(334)
print(a,b, type(a), type(b))

# camel case : myName = "Chetan"
# pascal case: MyName = "Chetan"
# snake case: my_name = "Chetan"

# assigning multiple values to multiple variables.
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

# assigning one value to multiple variables.

x = y = z = "Orange"
print(x,y,z)

# unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z) 


'''
Global variables:
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Use global keyword in function to use global variable inside function.

'''


