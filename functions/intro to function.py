def my_function():                # defining function
  print("Hello from a function")

my_function()                     # calling function

# parameters and arguments
"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

# *args = arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# keyword arguments = kwargs
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# arbitrary kwargs = **kwargs 
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("India")
my_function()

# return value
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))


# you can pass list, dictionary .. any data type as arguments.

# pass 
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

