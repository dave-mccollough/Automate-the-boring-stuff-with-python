# For loops
# Use when you need to loop a certain number of times
print('My name is')
for i in range(5):
    print('Jimmy five times ' + str(i))

total = 0
for num in range(101):
    total = total + num
print(total)

# While Loops
print('My name is')
i = 0
while 1 > 5:
    print('Jimmy five times ' + str(i))
    i = i + 1
    
# Range can have two values passed into it to determine range between them
# First value is where the for loop starts
# second value - up to but not including
print('My name is')
for i in range(12, 16):
    print('Jimmy five times ' + str(i))
    
    
# Range can also include step values
# They can be positive or negative
print('My name is')
for i in range(12, 16, 2):
    print('Jimmy five times ' + str(i))