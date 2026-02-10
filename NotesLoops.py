"""
Loops help us perform repetitve tasks, they are two types of loops
while loop
for loop
these loops enable us to easily repeat tasks other than writing countless lines of code
"""

"""
The while loop:
It is used to execute a block of statements 
repeatedly until a given condition is satisfied. 
"""
#Example:
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
#Once count becomes 5 the statement "count < 5" becomes false
#Because 5 is not less than 5 so the loops stops we can use "else" 
#If you want to continue running code once the loop has stopped

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

#We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3: 
        break #Basically meaning once we hit 3 stop the loop

#With the continue statement we can skip the current iteration, and continue with the next:

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue #basically after hitting 3 add 1 and contiue to loop up until the condition has been met
    print(count)
    count = count + 1

#The for loop's main objective is to iterate over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
 
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])