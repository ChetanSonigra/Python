# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

"""
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
""" 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict['year'])
print(len(thisdict), type(thisdict))

# key should be immutable i.e. strings, int, etc.

# access items
print(thisdict['year'])
print(thisdict.get('year'))
print(thisdict.get('dsf'))      # returns None if key not present.
print(thisdict.get('dsfsf', 55))
x = thisdict.keys() ; print(x)
x = thisdict.values(); print(x)
x = thisdict.items() ; print(x)

# change items
thisdict['year'] = 2014
print(thisdict)
thisdict.update({'year': 2020}); print(thisdict)

# adding item with assign or update method
thisdict['color']= 'red'
thisdict.update({'price': 44334324})
print(thisdict)

# remove  items
thisdict.popitem()          # removes last added item
thisdict.pop('color')
thisdict.clear()
del thisdict

# loop through dictionaries
# x in thisdict, x in thisdict.keys, x in thisdict.values, x in thisdict.items


# copy dictionary
"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy()."""

mydict = dict(thisdict); print(thisdict)
d = thisdict.copy(); print(d)

# nested dictionaries can be made by putting dictionaries in values.

# methods:
# get, clear, copy, pop, popitem, keys, items, values, update, setdefault

