""" Commented out for easy run of the other codes
#Conditional Test - TRY 5.1 to 5.2 
car = 'camry'
print(f"Is car == 'camry'?")
print(car == 'camry')

print(f"\nIS car == 'audi'? I predict False.")
print(car == 'audi')

print('mantle'.title() == 'mantle') 

age_1 = 21
age_2 = 24

print(age_1 > 20 or age_2 > 23)
print(age_1 > 21 and age_2 > 24)

"""

# IF Statements - TRY 5.3 to 5.7 
alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color == 'green':
        print("You just earned 5 points")

for color in alien_color:
    if color != 'blue':
        print('10 points have been deducted from your account')

for color in alien_color:
    if color != 'green':
        print("\nYou just earned 5 points")

#Alien colors #3
for color in alien_color:
    if color == 'green':
        print('Y0u just earned 5 points')
    elif color != 'green':
        print('You just earned 10 points')
    else:
        print('You have nothing to earn')

    
#stages of life
age = 10

if age < 2:
    print("You're a baby")
elif age >= 2 and age < 4:
    print("You're a toddler")
elif age >= 4 and age < 13:
    print("You're a kid")
elif age >= 13 and age < 20:
    print("You're a teenager")
elif age >= 20 and age < 65:
    print("You're an adult")
elif age == 65 or age > 65:
    print("You're an elder")

print("\n")

#Favorite fruits
favorite_fruits = ['banana', 'mango', 'apple', 'kiwi', 'pineapple']


for fruit in favorite_fruits:
    if fruit == 'banana':
        print(f"You really like {fruit}")
    if fruit == 'mango':
            print(f"You really like {fruit}")
    if fruit == 'kiwi':
            print(f"You really like {fruit}")
    if fruit == 'apple':
            print(f"You really like {fruit}")
    if fruit == 'pineapple':
            print(f"You really like {fruit}")

print("\n")

#TRY 5.8 to 5.11
#Hello Admin
usernames = ['john', 'tope', 'admin', 'isaac', 'kunle']
for user in usernames:
     if user == 'admin':
          print(f"Hello {user}, would you like to see a status report?")
     else:
        print(f"Hello {user}, thank you for logging in again.")
print("\n")

#No users
names = []
if names:
     for name in names:
          print({name})
else:
     print("We need to find some users!\n")

#Checking usernames
current_users = ['funsho', 'sade', 'mathew', 'alex', 'fred']
new_users = ['mathew', 'vivian', 'alexa', 'fred']

for user in new_users:
     if user.lower() in current_users:
          print("You need to enter a new username")
     else:
          print("The username is available")

print("\n")

#Oridnal Numbers 
ordinal = [value for value in range(1,10)]
for value in ordinal:
     if value == 1:
          print("1st")
     elif value == 2:
          print("2nd")
     elif value == 3:
          print("3rd")
     else:
          print(f"{value}th")
