"""
We're on the 3rd of the data structures. Sets are a collection of 
items which is typically un-ordered and un-indexed. Just think of them
like the sets in maths.
"""

#Creating Sets
sets = set()

#Creating a set with initial items
My_Set = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

print(len(fruits))

#Accessing items in a Set
print("mango" in fruits)

#Adding Items to a Set
fruits.add('kiwi')
fruits.add('lime')
print(fruits)

#You can add multiple items using update()
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

#Removing an item from a set
fruits.remove('mango')
print(fruits)
#If the item not in set and you use remove() it will raise an error
#However if you use discard() no error will occur 

#pop() removes an item and returns it
removed_item = fruits.pop()
print(removed_item)

#using the clear() method clears/emptys the set
fruits.clear()
print(fruits)

#del just like in lists and tuples deletes the set
del fruits

#Converting a list to a set
lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
stss = set(lst)
print(stss)

#Joining sets
st1 = {'item1', 'item2', 'item3', 'item4', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# returns a set of items which are in both sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2

#Subset and superset
"""
In Python, the issubset() method is a built-in function 
used with sets to check if all elements 
of one set are present in another set or iterable
"""
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True all the items in st2 are in st1
st1.issuperset(st2) #True

"""
issuperset() checks if one has all the elements of another 
basically checking is st1 contains all the elements in st2 which is correct
"""
# It returns the difference between two sets or using - symbol
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

