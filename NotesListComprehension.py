"""
List comprehension this is the faster method of creating a new list other than using a for loop
"""
#Example
#Lets say you want to change a stringinto a list of characters

#Method 1

language = 'Python'
lst = list(language) #Usual method we use changing a string to list of characters
print(type(lst)) # list
print(lst) # ['P', 'y', 't','h', 'o', 'n']

#Method 2
#Using list comprehension
Lsts = [i for i in language] #What this means the first 'i' is storing it in the list while the second is looping through the string
print(type(Lsts))
print(Lsts)

#You can also generate a list of numbers

#Generating numbers
numbers = [i for i in range(11)] #Generating from 0 to 10 (remember 11 is excluded)
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Mathematical operations are also doable 
sqaures = [i * i for i in range(11)]
print(sqaures) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#List of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#Combining List comprehension with if statements 

even_numbers = [i for i in range(21) if i % 2 ==0]
print(even_numbers) #[0, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18, 20]

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Filtering out postive even numbers
numberss = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
postive_even_numbers = [i for i in numberss if i % 2 == 0 and i > 0]
print(postive_even_numbers) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Flattening a two dimensional array
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattended_list = [number for row in list_of_list for number in row]
print(flattended_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]