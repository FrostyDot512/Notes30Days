"""
Tuples are one of the 4 main built-in data structures in Python 
just like lists they are ordered meaning data is got from index's
but one unique difference is that its unchangeable (immutable), meaning
you can't edit the data you either have to make sure its correct before completion or
convert it into a list or set or dictioanry then change it back
tuples use () brackets tuples only have 3 methods;
tuples() create empty tuple
count() count the number of items in tuple
index() find the index of a specified item in a tuple
+ to join two or more tuples to create a new one 
"""

#Creating an empty tuple
empty_tuple = tuple()

#With initial values:
tpl = ('item1', 'item2', 'item3', 'item4')
fruits = ('banana', 'orange', 'mango', 'lemon')

tpl_length = len(tpl)
print(tpl_length)

#Accessing items:
first_item = tpl[0]
second_item = tpl[1]
#Also uses negative index to start from end to start

#Slicing tuples
all_items = tpl[0:4] #all the items
all_items = tpl[0:] #all the items
middle_two_items = tpl[1:3]
print(middle_two_items) #Remember it only stops at 2 doesn't include index 3

#Changing them into lists

lst = list(fruits)
lst[0] = 'apple'
print(lst)

#uSING the in operator 
print('orange' in fruits)

#combining tuples
both_tpl = fruits + tpl
print(both_tpl)

#deleting tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1

