#statistics module

from statistics import *
ages= [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages)) #This calcuates standard deviation from a sample of data

import math

print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

#String Module

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#random module

from random import random, randint
print(random())
print(randint(5, 20))