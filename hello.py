print('Hello World')

print('What is your name') #Ask for their name
# input() gets input from the user - Always a string
myName = input()
print('It is good to meet you,' + myName)
print('The length of your name is:')
# len gets length of string
print(len(myName))

print('What is your age?') #Ask for their age
myAge = input()
# to convert input string to integer, use int(string to convert to integer)
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
