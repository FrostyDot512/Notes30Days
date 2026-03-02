"""
We already covered how to create modules and importing them, now we're looking at 
importing functions from a module
"""

"""
example:

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name("Anwaar", "Batala"))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

what we were doing here is taking functions from the module "mymodule" and importing the functions 
"""

"""
we can also import functions from the modules and rename them to whatever we want
from mymodule import generate_full_name as fullname, sum_two_numsas total, person as p, gravity as g
print(fullname("Anwaar", "Batala"))
print(total(1,9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

we renamed the functions with alternative names generate_full_name becomes fullname, person becomes p and so on.
"""

#Python has many inbuilt operating systems such as math, os, datetime, sys, random, statistics, collects, json, re

#The os module
#This mainly helps with dealing with operating system tasks, provides functions in creating, changing working directory
#and removing a directory (folder)fetching its contents, changing and identifying the current directory