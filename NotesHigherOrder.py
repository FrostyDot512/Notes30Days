"""
In Python functions are treated as high class citizens enabling us to do various work
such as;
1. Take one or more functions as paramaters
2. Function can be returned as a result of another function 
3. Function can be modified
4. Function can be assigned to a variable 
"""
"""
In high order functions we will cover; 
handling them as paramters
returning functions as return value from another functions 
using python closures and decorators
"""

#Function as a paramter

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst): # In this case the f stands for function
    summation = f(lst) # Were calling the function here
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

#Function as a return value
def sqaure(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_FunctionMath(type): #Higher order function returning function
    if type == "sqaure":
        return sqaure
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute
    
resultAgain = higher_order_FunctionMath('sqaure')
print(resultAgain(3))
resultCube = higher_order_FunctionMath('cube')
print(resultCube(3))
resultAb = higher_order_FunctionMath('absolute')
print(resultAb(3))

#Will deal with closures and decorates later

#Built it higher order functions 
#Built in higher order functions include map(), filer and reduce 

#The map function takes a function and iterable as paramters

numbers = [1, 2, 3, 4, 5]
def sqauresAgain(x):
    return x ** 2

numbers_sqaured = map(sqauresAgain, numbers) #Remember an iterable is anything that can be looped over
print(list(numbers_sqaured)) # [1, 4, 9, 16, 25]
#Lets apply it with a lambda function 
numbers_sqaured = map(lambda x : x**2, numbers)
print(list(numbers_sqaured))

#Example 2

numbers_str = ['1', '2', '3', '4', '5'] #iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int)) # [1, 2, 3, 4, 5]

#Example 3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] #iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))
#Iterates over a list, changes the names to upper case and returns a new list

#Python Filter Function 
#In simple terms the filer() functions filters out items which fit the filtering criteria 

#Example 
NumbersYes = [1, 2, 3, 4, 5] #iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, NumbersYes)
print(list(even_numbers)) # outputs [2, 4]

#Example 2 

IsName = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def is_name_long(nameD):
    if len(nameD) > 7:
        return True
    return False

long_names = filter(is_name_long, IsName)
print(list(long_names))

#Reduce Function 
#Compared to filer() and map reduce() only returns a single value

"""
numbersSTR = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbersSTR)
print(total)
"""