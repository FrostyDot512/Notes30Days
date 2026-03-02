import random 
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = " "

    for i in range(6):
        user+= random.choice(characters)

    return user_id

print(random_user_id())