
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

# to access item in a list
print(spam[1])

# list within a list
spam1 = [['cat', 'bat'], [1,2,3,4]]
print(spam1[0]) #['cat', 'bat']
print(spam1[0][1]) #bat

# Negative list values
spam2 = ['cat', 'bat', 'rat', 'elephant']
print(spam2[-1]) #elephant
print(spam2[-4]) #cat

# Slice - assigns to a new list value
spam2 = ['cat', 'bat', 'rat', 'elephant']
# starts at 1 and goes up to, but does not include the value at 3
print(spam2[1:3]) #['bat', 'rat']

# Assign new values to items of an list
spam3 = ['cat', 'bat', 'rat', 'elephant']
spam3[1] = 'hello'
print(spam3) #['cat', 'hello', 'rat', 'elephant']

# Assign new values to list via slice
spam4 = ['cat', 'bat', 'rat', 'elephant']
spam4[1:3] = [1,2]
print(spam4) #['cat', 1, 2, 'elephant']

# Leaving out slice values - blank implies 0
print(spam4[:3]) #['cat', 1, 2]

# to delete an item from a list, use the del keyword
del spam4[2]
print(spam4) #['cat', 1, 'elephant']

# to get the length of a list
print(len(spam4)) #3

# To check if value in list
'cat' in spam4
print('cat' in spam4) #True

