"""
In this course we've dealt with in-built functions, but you can also create your own functions. 
This is useful when you have a piece of code that you want to reuse multiple times in your program. By defining a function, 
you can give it a name and then call it whenever you need to execute that piece of code.
"""
# Here's how you can define a function in Python:
def generate_full_name():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(full_name)
generate_full_name() # This will call the function and print "John Doe"

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers() # This will call the function and print 5

# Functions also return values. This means that instead of just printing the result, you can return it to be used elsewhere in your program.
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

def generate_full_name():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    return full_name

# Functions with parameters allow you to pass in values when you call the function, making it more flexible and reusable.
# Single parameter function

def greetings(name):
    message = "Hello, " + name + "!"
    return message
print(greetings("Alice")) # This will print "Hello, Alice!"

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(5)) # This will print 15

# Multiple parameters function

def generate_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name
print('Full Name:',generate_full_name('John', 'Doe')) # This will print "Full Name: John Doe"

def sum_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total
print('Sum:',sum_two_numbers(5, 10)) # This will print "Sum: 15"

# Passing arguments with Key and Value

def generate_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name
print('Full Name:',generate_full_name(first_name='John', last_name='Doe')) # This will print "Full Name: John Doe"

#Quick side note:
# Printing is just for displaying output to the user, while returning a value allows you to use that value elsewhere in your program.

# Function with default parameters

def greetings(name='Guest'):
    message = "Hello, " + name + "!"
    return message
print(greetings()) # This will print "Hello, Guest!"
print(greetings('Alice')) # This will print "Hello, Alice!"
# This basically means that if you call the function without providing a value for the parameter, it will use the default value specified in the function definition.

def generate_full_name(first_name='John', last_name='Doe'):
    full_name = first_name + " " + last_name
    return full_name
print('Full Name:',generate_full_name()) # This will print "Full Name: John Doe"
print('Full Name:',generate_full_name(first_name='Alice', last_name='Smith')) # This will print "Full Name: Alice Smith"

def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age
print('Age:', calculate_age(1990)) # This will print "Age: 31"
print('Age:', calculate_age(1990, current_year=2022)) # This will print "Age: 32"

# Arbitrary number of parameters
# Sometimes you may want to create a function that can accept any number of parameters. In Python, you can use *args to achieve this.

def sum_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print('Sum:', sum_all_numbers(1, 2, 3, 4, 5)) # This will print "Sum: 15"

def generate_groups(teams, *args):
    print(teams)
    for i in args:
        print(i)
generate_groups('Team-1', 'John', 'Brook', 'David', 'Eyob')
