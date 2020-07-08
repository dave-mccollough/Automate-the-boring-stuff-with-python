spam = 42 #global variable

def eggs():
    spam = 42 #local variable
    
# ------Code in the global scope cannot use local variables
def spam():
    eggs = 99
# eggs is a local variable, so it can't be used globally
spam()
print(eggs)

# ------Code in one functions local scope cannot use variables in any other local scope
def spam1():
    eggs = 99
    bacon()
    print(eggs)
# Eggs in this function are seperate from eggs in this function 
def bacon():
    ham = 101
    eggs = 0
    
spam1()
# for variables defined in functions
# Assignment Statement = Local Variable
# No Assignnment Statement = Global Variable

# ------to assign a local variable as global, define the variable as global:  global eggs
def spam3():
    global eggs
    eggs = 'Hello'
    print(eggs)
    
eggs = 42
spam3();
print(eggs)