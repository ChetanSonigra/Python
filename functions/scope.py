# local scope:
"""A variable created inside a function belongs to the local scope of that function, and can only be used inside that function."""

# function inside function:
x = 3
def myfunc():
  x = 300
  def myinnerfunc():
    nonlocal x                    # outside function but not global = nonlocal                      # global space
    x += 33
    print(x)
  myinnerfunc()
myfunc()


# global scope
"""A variable created in the main body of the Python code is a global variable and belongs to the global scope."""
x = 300
def myfunc():
  print(x)
myfunc()
