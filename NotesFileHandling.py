"""
File handling is one of the most essential components when it comes to prgramming, since we deal with multiple file
formats such as (txt, json, xml, csv,tsv,excel) file handling helps us read, update and delete files
We use the built in function open()
"""

"""
r = read (Opens and reads a file, returns error if file doesn't exist)
a = append (Opens a file for appending, creates a file if it doesn't exist)
w = write (Opens a file for writing, creates a file if it doesn't exist)
x = create (Createsa specified file, returns an error is file exists)
t = text (Text Mode)
b = binary (Binary Mode eg images)
"""

#Opening Files for Reading 

f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
# An opened file has many methods but remember after opening it don't forget to always close it
# read(), readline, readlines

# read()
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# readline() only reads the first line of an opened file
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines() Read all the text contained and return as a list
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to read all the text and return it as a list is splitlines()
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

#There is a tendency of not closing the file so using the keywork with helps alot 
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# Opening Files for Writing and Updating 
# a is for append it will append(write) a the end of the file, if the file doesn't exist it creates
# w is for write, this one will overwrite the current existing content, if file doesn't exist it creates

with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

# Deleting Files
# We use the os module for helping in the deleting of files
    
import os 
os.remove('./files/example.txt')

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

# txt aren't the only files we deal with we also deal with json (JavaScript Object Notation)
# Changing JSON to Dictionary

import json
person_json = '''{
"name": "Asabeneh",
"country": "Finland",
"city": "Helsinki",
"skills": ["JavaScript", "React", "Python"]
}'''

# Let's change JSON to dictionary 
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct)

# Changing Dictionary to JSON

import json
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skill": ["JavaScript", "React", "Python"]
}

# lets conver to json
person_json = json.dumps(person, indent = 2)
print(type(person_json))
print(person_json)

# Saving as JSON file
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
