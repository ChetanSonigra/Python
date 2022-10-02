# tuple is ordered, indexed, immutable and allows duplicate values.

mytuple = ("apple", "banana", "cherry", 34, 454,True, True, 4.44)
print(mytuple,type(mytuple),len(mytuple))

# accessing items in tuple with slicing and indexing

# in , not in for checking whether item is in tuple.

# add, edit , delete item from tuple
l = list(mytuple)
l[1] = "bananas"
mytuple = tuple(l); print(mytuple)

l.append('DKJ')
mytuple= tuple(l)
mytuple += ("sd",); print(mytuple)

l.remove('DKJ')
mytuple = tuple(l); print(mytuple)
del mytuple # delete tuple completely

# unpack tuple values
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# join, multiply tuples
t = fruits+mytuple ; print(t)
t2 = fruits*2; print(t2)

# methods
print(t2.count('papaya'))
print(t2.index('mango'))

