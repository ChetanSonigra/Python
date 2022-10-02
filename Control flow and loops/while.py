i = 1
while i < 6:
  print(i)
  i += 1

# break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else statement
# The else block will NOT be executed if the loop is stopped by a break statement.         
i = 1
while i < 6:
  if i ==2:
    i += 1
    continue
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i = 1
while i < 6:
  if i ==2:
    i += 1
    break
  print(i)
  i += 1
else:
  print("i is no longer less than 6")