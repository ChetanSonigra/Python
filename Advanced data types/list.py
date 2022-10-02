# list are mutable, ordered collection.
# list allows duplication.

"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

l = [33, "dsfds", 5j, True, None]
print(type(l))
print(len(l))

# access list items, change list items.
print(l[1], l[:2])
# change list items.
l[1] = 444
# insert :
l.insert(1, 'KSDJFL')
print(l)
m = [1,2,3,444]
l.append(m)
l.extend(m)
print(l)

# l.pop(index) = removes based on index
l.pop(13)

# l.remove(3) = removes first element found which is 3
l.remove(444)
print(l)

# del any element of list or full list completely. it removes the object.
del l[6]
print(l)
del l
print(l)

# clear - it only clears values in list, not delete list object.
l = [11,3,55,324, "fhdskjh"]
l.clear()
print(l)

# Looping through list
for i in range(len(l)):
    print(l[i])
for x in l:
    print(x)

# list comprehension
# newlist = [expression for item in iterable if condition == True]
l2 = [x for x in l if isinstance(x, int)]
print(l2)

# sort list
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
l2.sort(key = lambda x: x%5)
print(l2)                                  #key - any function

print(sorted(l2)) # returns new list

# copy the list
l3 = l2.copy()
l4 =  list(l2)
print(l3,l4)

# join list
l3 = [4,5,6]
l4 = l3 + l2; print(l4)
l3.append(l2); print(l3)
l3.extend(l2); print(l3)

# list methods
# append,extend, clear, index, count, copy, reverse, pop, insert, remove, sort