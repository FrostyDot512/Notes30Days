"""
We've finally reached the end of the data structures and we end on 
Dictionaries
they are unordered and un-indexed, mutable and use key pair values
examples;
{'age': 18} Age is the key and the pair is 18
"""
# We can create using {} or the built in dict() function
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#Clear Example:
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
#Remember a comma at the end of each pair instead of the end
#Stores multiple data types

#Length
print(len(dct)) #Answer is 4
# When counting (I think) they count the data type

#Accessing Dictionary Items
#We access them by referring to its key name.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
#This method is faulty however because if the key is not in the 
#dictionary an error will form thats why the get() method is used if the 
#key is not in the dictionary None is returned which is a NoneType object data type

print(dct.get('key1'))
print(dct.get('key5'))

#Adding items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5' 

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

#Modifying
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Eyob'
person['age'] = 252

#Using the in operator 
print('key2' in dct)
print('key5' in dct)

"""
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name (basically the same as pop(key)) 
"""
#The items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Obvious what clear() and del() do and copy()

# Gives us a list of keys only
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

#Gives us a list of values only 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

#A quick note when they say create a dictionary thats when you do:
"""
student_dictionary = {
'first_name': 'Noah'
'last_name': 'Olweny'
'Age': 17
'School': 'Maria Hall Hill'
}
"""
#You do that but when they say add stuff into a dictionary you do:
"""
dog = dict()
dog['Name'] = 'Henry'
dog['Color'] = 'Brown'
dog['Breed'] = 'German Sherpad'
dog['Legs'] = 4
dog['Age'] = 5
#3
"""
#Thats the difference 
