name = 'Alice'
if name == 'Alice':
    print('Hi Alice!')
print('Done')    

name = 'Bob'
if name == 'Alice':
    print('Hi Alice!')
print('Done')    

# if and else
password = 'swordfish'
if password == 'swordfish':
    print('Access Granted')
else:
    print('Wrong Password')   

# elif
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo!')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, Grannie.')
    
# Truthy and Falsey
# Checks to see if 'name' variable is blank
print('Enter a name')
name = input()
# should use if name != '': instead of if name:
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')
    
# The values 0, 0.0, and empty strings are considered to be falsey values
# You can test truthy and falsey values by passing them to a bool() function
    
