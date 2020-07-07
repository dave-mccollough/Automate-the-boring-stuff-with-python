# return random integer between int a and int b
import random
print(random.randint(0,9))

# can import multiple builtin functions on one line
import os, math, sys
# To import entire function library
# not recommended due to poor readability
from random import *
randint(0,10)
# To exit a program
sys.exit()

# Python has several third modules can be installed via pip
# https://automatetheboringstuff.com/appendixa/
# pip install pyperclip
# pyperclip copies and pastes text to and from clipboard
import pyperclip
pyperclip.copy("hello world")
pyperclip.paste()
