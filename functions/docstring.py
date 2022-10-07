"""Python docstrings are the string literals that appear right after the definition of a function, method, class, or module"""
# use ''' or """ to create docstring.
import math 
print(math.__doc__)
print(math.sqrt.__doc__)

# If we do not assign strings to any variable, they act as comments.
"jnwewbjsfijg"


# user defined docstring :
class Person():
    """class representing a person."""
    def __init__(self, name, height=5.5 , weight = 60):
        self.name = name
        self.height = height
        self.weight = weight
    def speak(self):
        return f"Hello, I am {self.name}"

print(help(Person))
print(Person.__doc__)


# docstring for python packages:
# The docstrings for a Python package is written in the package's __init__.py file.

"""help() function retrieves the docstrings of the class along with the methods and data descriptors asociated with that class."""


# docstring format:
#           google/Sphinx , Epytext , reST(restructured text), Numpydoc



# Automaically generate or convert docstring from format to another one with pyment.