print('In every programming language there is \"Hello world\"')
print("This is a test checking the \'double qoutes\'")

#Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string1 = 'The area of circle with a radius %d is %.2f.' %(radius, area) 
print(formated_string1)
# 2 refers the 2 significant digits after the point

"""
Purpose: It allows dynamic string creation, 
controlling decimal places, alignment, and formatting, 
serving as a more efficient alternative to manual string concatenation. 
"%"
In other terms its another way of embedding varibales into string texts without the whole
concatenation nonesense, it works with the use of tuples btw.
One thing to remember that Python strings are series of characters 
"""
#Creation of a new string method 

first_name1 = 'Asabeneh'
last_name1 = 'Yetayeh'
language1 = 'Python'
formated_string2 = 'I am {} {}. I teach {}'.format(first_name1, last_name1, language1)
print(formated_string2)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) 
# 2 digits after decimal
print(formated_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

"""
One thing that confuses alot that:
Python counting without index it normal eg. Python is 6 but if were counting using index?
Then it's 5 because we start counting from 0. So basically len(Python) = 6 but then when 
using index it only has up to 5 [0][1][2][3][4][5] 
"""

#Reversing strings
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

#Count the number of occurances of substring in a string count(substring, start=, stop=)
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

