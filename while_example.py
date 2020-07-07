spam = 0
while spam < 5:
    print('Hello World!')
    spam = spam + 1
    
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# Break statement - causes loop to end 
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name != 'your name':
        break
print('Thank you!')

# Continue statement - causes loop to restart and reevaluate condition
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        # continue will cause loop to restart before executing print statement
        continue
    print('Spam is ' + str(spam))

# You can use control c to break out of a loop