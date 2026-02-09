"""
We're finally on Conditionals, this is where the if, else and elif 
statements come about
We gotta remember that in python code is run from top to bottom however 
conditinal and repetitive execution can alter this
"""

#If statements
#used to check if a condition is true and to execute the block code.
#Example:
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number the condition was correct meaning 
#the block of code was executed, if it was false no code would have been executed
#In order to see the result of the falsy condition, 
# we should have another block, which is going to be else.

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#Using elif statements 

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Nested Conditions

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#If condition and logical Operators

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')