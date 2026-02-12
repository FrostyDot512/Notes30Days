#Level 1
#1

Enter_Age = int(input("Enter your age: "))
if Enter_Age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f"You need {18 - Enter_Age} more years to leaen to drive")

#2

my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print('You are 1 year older than me')
    else:
         print(f'You are {your_age - my_age} years older than me')
elif my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print('I am 1 year older than you')
    else:
        print(f"I am {my_age - your_age} years older than you")
else:
    print(f"We both are the same age. {your_age} years old")

#3

letter_a = int(input("Enter Number1: "))
letter_b = int(input("Enter Number2: "))
if letter_a > letter_b:
    print(f"{letter_a} is greater than {letter_b}")
elif letter_b > letter_a:
    print(f"{letter_a} is greater than {letter_b}")
else:
    print(f"{letter_a} and {letter_b} are equal")

#Level 2


student_grade = int(input("Enter student grade: "))
if student_grade >= 90 and student_grade <=100:
    print("A")
elif student_grade >=80 and student_grade <=89:
    print("B")
elif student_grade >=70 and student_grade <=79:
    print("C")
elif student_grade >=60 and student_grade <=69:
    print("D")
elif student_grade >=0 and student_grade <=59:
    print("F")

#2

month_given = input("Enter month: ").capitalize
if month_given in ["September", "October" ,"November"]:
    print("Season: Autumn")
elif month_given in ["December", "January", "February"]:
    print("Season: Winter")
elif month_given in ["March", "April", "May"]:
    print("Season: Spring")
elif month_given in ["June", "July", "August"]:
    print("Season: Summer")
else:
    print("Invalid Month")

#Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

#2
if "skills" in person:
    skills = person['skills']
    if "Python" in skills:
        print("Python is in Skills")
    else:
        print("No Python in skills")

#3
if 'skills' in person:
    skills = set(person['skills'])   
    if {'JavaScript', 'React'}.issubset(skills):
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')

#4
if person['is_married'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")