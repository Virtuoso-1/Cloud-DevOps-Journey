#Files and Exceptions
#Importing program/module from the python library - Try it yourself 10.1 to 10.3 
from pathlib import Path 

path = Path('/home/olamide/DevOps/ltc/python/text.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


#10.2 - Learning C
#Replacing the word 'Python' with 'C' in the contents variable.

details = path.read_text()
details.replace('Python', 'C')
print(details)

""" 
Troubleshooting -- the replace method is nof working right now. 
message = "I really like dogs"
message.replace('cat', 'dog')
print(message)
"""

#10.3 - Simpler Code : Removing the temporary variable lines
for line in details.splitlines():
    print(line)

"""
#Try it yourself 10.4 to 10.5 
question = "What is your name?"
question += "Kindly respond in this format: Firstname Lastname  "
response = input(question)

file = Path('/home/olamide/DevOps/ltc/python/guest.txt')
file.write_text(response)

"""

"""Commented out to work with other tasks. 
#10.5 - Guest book
question = "What is your name?"
question += "Kindly respond in this format: Firstname Lastname  "
question += "Enter 'q' to quit"


poll = True
answer = ''
while poll:
    response = input(question)
    if response == 'q':
        poll = False
    else: 
        answer += (f"{response}\n")

file = Path('/home/olamide/DevOps/ltc/python/guest.txt')
file.write_text(answer)

"""

"""
#Exceptiions - Try it yourself 10.6 to 10.10
#10.6 - Addition: Prompting user fot two numbers and adding them together.
first_num = input("Give me two numbers and I will add them together. " \
                    "First Number: ")
second_num = input("Input your second number: ")

try:
    addition = int(first_num) + int(second_num)
    print(f"The addition of the two numbers is: {addition} ")
except ValueError:
    print(f"Invalid literal. You have to input number in base 10.")


"""

"""
#10.7 - Addition Calculator - Wrapping the code inside the while loop to asking 
#for number even when the input is invalid. 
while True: 
    first_num = input("Give me two numbers and I will add them together. " \
                    "First Number: ")
    second_num = input("Input your second number: ")


    if first_num == 'q' or second_num == 'q':
        break
    else:
        try:
            addition = int(first_num) + int(second_num)
            print(f"The addition of the two numbers is: {addition} ")
        except ValueError:
            print(f"Invalid literal. You have to input number in base 10.")


"""

"""
#Storing Data - Try it yourself 10.11 to 10.14 
#Favorite Number
import json

path2 = Path('/home/olamide/DevOps/ltc/python/favorite.txt')

fav_num = input("What is your favorite number: ")
fav_contents = json.dumps(fav_num)
path2.write_text(fav_contents)

contents = path2.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}")

"""


"""
#10.12 - Favorite Number Remembered
#Combining the 2 program above with if statements. 
from pathlib import Path 
import json

path2 = Path('/home/olamide/DevOps/ltc/python/favorite.txt')

if path2.exists():
    contents = path2.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")
else:
    fav_num = input("What is your favorite number: ")
    fav_contents = json.dumps(fav_num)
    path2.write_text(fav_contents)
    print(f"We'll remember your favorite number: {fav_num}")

"""

"""
#10.13  - User Dictionary 
from pathlib import Path
import json

path3 = Path('/home/olamide/DevOps/ltc/python/username.json')
if path3.exists():
    contents = path3.read_text()
    user_details = json.loads(contents)
    print(f"Welcome back, {user_details}!")
else:
    user_response = {}
    username = input("What is your name? ")
    age = input("What is your age? ")
    bmi = input("What is bmi? ")

    #Storing all the responses in the dictionary user_response
    user_response['username'] = username
    user_response['age'] = age
    user_response['bmi'] = bmi
    
    contents = json.dumps(user_response)
    path3.write_text(contents)
    print(f"\nWe'll remember you when you come back, {user_response}!")

"""

#10.14 - Verify User
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username   


def greet_user():
    """Greet the user by name"""
    path = Path('/home/olamide/DevOps/ltc/python/username1.json') 
    username = get_stored_username(path)
    print(username)
    confirm_user = input("Is this your correct username: yes/no  ")
    if username and confirm_user == 'yes':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()  











