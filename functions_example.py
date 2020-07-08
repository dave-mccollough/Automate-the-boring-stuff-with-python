# ------Functions------

def hello():
    print('Howdy')
    print('Howdy!!!')
    print('Hello There!!!')
    
hello()

#using parameter
def hello1(name):
    print('Hello ' + name)
# passing arguments
hello1('Dave')
hello1('Bob')

# using return function
def plusOne(number):
    return number + 1
newNumber = plusOne(12)
print(newNumber)
# Every function has a return value, if no declared return value, function returns none
# print takes in end and sep
print('Hello', end= '')
print('World')
# defines seperator between string
print('cat', 'dog', 'bird' , sep= '---')



