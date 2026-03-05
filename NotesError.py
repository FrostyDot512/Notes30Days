"""
When we write code they're moments where we experience errors because of a typo or any
other common error, the Python interpreter will display an error message containing feedback about the problem
and ways to solve it. Understanding different error messages will help us understand python better and debug 
our code much quicker 
"""

# Syntax Error (Basically meaning we have a typo in our code eg wrong spelling in an in-built function)
"""
print 'hello world' 
(You can clearly see this is an error because we forgot to add paranthesis onto the print, this is an example of an Syntax error)
*fixed*
print('hello world')
"""

# Name Error (This occurs when you try use a variable which has not been properly defined)
"""
print(age)
(This is wrong because we haven't declared the variable age is basically empty)
*fixed*
age = 25
print(age)
"""

# Index Error (This is a type of error when index is out of range eg when they're only 3 space but you do num[5])
"""
numbers[1, 2, 3, 4, 5]
numbers[5]
Doesn't make sense because it's only from 0 to 4 not 5
*fixed*
numbers[4]
"""

# ModuleNotFoundError (Occurs when trying to import a module which doesn't exist)
"""
import maths
the module maths doesn't exist
*fixed*
import math
"""

# Attribute Error (Trying to input an attribute from a module which doesn't exist)
"""
import math
math.PI
*fixed*
math.pi
"""

# Key Error (This is quite straight forward mainly happens with wrong spelling in key field)
"""
users = {'name': 'Asab', 'age': 23, 'country': 'Findland'}
users['county']
*fixed*
users['country']
'Finland
"""

# Type Error (Mixing two datatypes together)
"""
4 + '3'
*fixed*
4 + int('3')
7
"""

# Import Error (Importing the wrong functions with modules)
"""
from math import power
*fixed*
from math import pow
pow(2, 3)
8
"""

#Value Error (Typically occurs when a formula has the wrong type of argument)
"""
int(12a)
This won't because it has the letter 'a' in it
"""

# ZeroDivision Error (Self explanatory, dividing anything by 0)
"""
1/0
"""

