# Set items are unordered, immutable but can add/remove items, and do not allow duplicate values.

set1 = {"abc", 34, True, 40, "male"}
print(type(set1), len(set1))

# set constructor
thisset = set(("apple", "banana", "cherry")) 

# access item in set, you can not access item by index/key , but you can loop through it or check if item is inside set.
for x in set1:
    print(x)
print("banana" in thisset)

# add item in set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# add any iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist); print(thisset)

# remove items
# discard does not raise an error if item not present, remove raises an error.
thisset.remove('banana'); print(thisset)
thisset.discard('randjfdff')
thisset.pop()                         # removes random item

thisset.clear(); print(thisset)    # clears all item
del thisset    ; print(thisset)    # removes object

# Join 2 sets
set1 = {"a", "b" , "c", 2}
set2 = {1, 2, 3, 'a', 'b'}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2); print(set4)
set5 = set1.symmetric_difference(set2); print(set5)

# methods
# add, clear, copy, difference, difference_update, discard, intersection, 
# intersection_update, issubset, issuperset, pop, symmetric_difference, symmetric_difference_update, 
# remove, union, update, isdisjoint - checks whether sets have intersection or not.