
# range object
for i in range(4):
    print(i)
# 0
# 1
# 2
# 3
# is the same as
for i in [0, 1, 2, 3]:
    print(i)
# 0
# 1
# 2
# 3

# list(range(4))
list1 = list(range(4))
print(list1)
# [0, 1, 2, 3]

# to list a range with a step count(count by 2)
step_count = list(range(0,100,2))
print(step_count)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 
# 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 
# 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 
# 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# You can use range and len to loop through a list
supplies =['pen', 'paper', 'binder', 'flamethrower']
for i in range(len(supplies)):
    print('index ' + str(i) + ' in supplies is: ' + supplies[i])
# index 0 in supplies is: pen
# index 1 in supplies is: paper
# index 2 in supplies is: binder
# index 3 in supplies is: flamethrower

# multiple assignments
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
sound = cat[2]
# Instead you could do the following
size2, color2, sound2 = cat
print(size2, color2, sound2) #fat orange loud
# or you could do
size3, color3, sound3 = ['round', 'red', 'quiet']

# Swapping variables
a = 'AAA'
b = 'BBB'
a, b = b, a

# Augmented assignment operators
spam = 42
spam += 1
print(spam)
