"""
The best way for me to describe what exception handling is, its the safe handling to prevent
the the applications from crashing basically. Often times the programs prints a descriptive 
error message to a terminal or log as part ofthe graceful exit. The keywords used in exception
handling are;
try
except
else
finaly
"""

"""
try:
    (Run this Code)
except:
    (Excute this code when there's an error, if things go wrong)
else:
    (No exceptions? Run this code)
finally:
    (Always run this code)
"""
#Example

try:
    name = input("Enter your name: ")
    year_born = input('Year you were born: ')
    age = 2026 - year_born
    print(f"You are {name}. And your age is {age}.")
except:
    print('Something went wrong')

#In the above example the exception block will run but we don't know the exact problem
#To identify the problem we can use different error types to help us 
    
try:
    NameAgain = input("Enter your name: ")
    year_bornAgain = input('Year you were born: ')
    ageAgain = 2026 - year_bornAgain
    print(f"You are {NameAgain}. And your age is {ageAgain}.")
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('ZeroDivision error occured')

#The code above the error produced is TypeError now adding the additional block
    
try:
    NameAgainA = input("Enter your name: ")
    year_bornAgainA = input('Year you were born: ')
    ageAgainA = 2026 - int(year_bornAgain)
    print(f"You are {NameAgainA}. And your age is {ageAgainA}.")
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('ZeroDivision error occured')
else:
    print('I usally run with the try block')
finally:
    print('I always run')

#Also shortned to 
    
try:
    nameYes = input('Enter your name: ')
    year_bornYes = input('Enter your name: ')
    ageYes = 2026 - int(year_bornYes)
    print(f'You are {nameYes}. And your {ageYes} years old')
except Exception as e:
    print(e)

#Packing and Unpacking Arugments in Python
"""
We use *for tuples
And we use **for dictionaries
"""
#Unpacking 
#Unpacking Lists
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) #Type error will occur because the function missing 4 other arugment
# b, c, d, e takes numbers not a list as arugments considers the list as one arugment

def sum_of_five_numsSA(a, b, c, d, e):
    return a + b + c + d + e

lstAgain = [1, 2, 3, 4, 5]
print(sum_of_five_numsSA(*lstAgain)) # We unpacked the list

# A list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last) # 1 [2, 3, 4, 5, 6,] 7

#Unpacking Dictionaries

def Unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old'
dct = {'name': 'Anwaar', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
print(Unpacking_person_info(**dct)) # Anwaar lives in Findland, Helsinki. He is 25 years old

#Packing
#Packing Lists
"""
Sometimes we don't know how many arugments will be passed so we use args and kwargs to help us
it allows us to take an unlimited number or arbitrary number of arguments
"""
def sum_all(*args):
    s = 0
    for i in args:
        s += i
        return s
print(sum_all(1, 2, 3)) # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7,)) # 28

#Packing dictionaries

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packing_person_info(name='Anwaar', country='Finland', city='Helsinki', age='25'))

#Zip

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)