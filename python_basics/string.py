# single quote or double quote
a = "test"
b = 'test'

# multiline string
 
s = """sdlkfj
sdfh
fdsh
"""
print(a,b,s)

# strings are array

# indexing and slicing :
print(s[::-1])
print(s[3])

# looping through string:
for x in s:
    print(x)

# in or not in string: 
if 's' in s:
    print(True)
if 'a' not in s:
    print(False)