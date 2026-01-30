"""
List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

Okay when they talk about it being ordered or unorderd, they're
talking about how in Lists and Tuples the order matters, keeps items in the
order you added them and you access them through index. However for 
Sets and Dictionaries don't care about the order theres' no "first" item.
Best example to use for ordered Numbered seats in a bus. Everyone has a fixed spot
Best for unordered items thrown into a bag. No assigned spots
"""
"""
A list is collection of different data types which is ordered and modifiable(mutable). 
A list can be empty 
or it may have different data type items.
"""

#They are two ways in creating lists either using the 
#built-in function or using sqaure brackets 

empty_list = list() #Empty list, having no items in it
print(len(empty_list)) #Outputting 0

#Using Sqaure brackets

empty_list1 = []
print(len(empty_list1)) #Same output as above

#With inital values and finding length:

fruits = ['banana', 'orange', 'mango', 'lemon']  
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

#Quick note that lists can have mutlple data types within them
"""
Unpacking a list: 
This basically means removing items from a list and assigning it onto different
variables on one single line. "List unpacking is assigning elements of a list to multiple variables in a single statement."
"""
#Example of unpacking: 

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
#A question may arise asking whats the use of the aristik? It basically means,
#grab everything that remains so item1 is given to first, then item2 is given to second
#then item3 is given to third then we use rest to collect item4 and 5 and basically make a new list

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
#When values are getting sliced this is the order (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
#So start, end (remember the end is length -1), then the step either skip 1 step, 2 steps etc

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

#We add items onto a list using the keyword append()

fruits1 = ['banana', 'orange', 'mango', 'lemon'] 
fruits1.append('apple')
print(fruits1)
#Btw when we use append() it adds the item at the end of the List

#Now when we use the keyword insert() it adds it in a specified index

fruits1 = ['banana', 'orange', 'mango', 'lemon'] 
fruits1.insert(2, 'apple') #inserts it between orange and mango
print(fruits1)

#Keyword remove() removes a specified item from list while
#pop() removes the last value added onto the list if not speicifed or removes from specified index
#del() removes the specified index or index range or the list itself 






