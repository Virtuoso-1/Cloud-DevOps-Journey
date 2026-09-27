#User Input and While Loops
"""
message = input("What is your name?")
print(message)


#Try it yourself - 7.1 to 7.3
#Rental car
car = input("what kind of rental car would you like?")
print(f"Let me see if I can find you a {car}")

#Restaurant Seating
group_size = input("How many are you in the dinner group?")
group_size = int(group_size)

if group_size > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready")



#Multiples of ten
random_num = input("input any number and I tell if it is random or not")
random_num = int(random_num)

if random_num % 10 == 0:
    print("the number is a multiple of 10")
else:
    print("the number is not a multiple of 10")

print("\n")


#Try it yourself - 7.4 to 7.7
prompt ="Please enter the list of toppling you want: "
prompt += "Enter quit to stop"

while True:
    pizza_toppling = input(prompt)
    if pizza_toppling == 'quit':
        break
    else:
        print(f"You'll add {pizza_toppling} to your pizza\n")



#Movie tickets - 7.5
message = "Please input your age. "
message += "Enter 0 to quit: "

while True:
        age = input(message)
        age = int(age)
        
        if age == 0:
             break
        
        elif age <= 3:
            print("Your movie ticket is free")
        elif age >= 3 and age <= 12 :
            print("The movie ticket is $10")
        elif age > 12:
            print("The movie ticket is $15")


#Try it yourself - 7.8 to 7.10
sandwich_orders = ['vanilla', 'chocolate', 'strawberry', 'banana']
finished_sandwiches = []

#7.9 - No Pastrami 
sandwich_orders.append('pastrami')
sandwich_orders.insert(0, 'pastrami')
sandwich_orders.insert(2, 'pastrami')

print(sandwich_orders)

print("deli has run out pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Now running the order
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nThese are the all the sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)


""" #end of comment
    

#7.10 - Dream Vacation
responses = {}
#Set a flag to indicate that polling is active 
polling_active = True

while polling_active:
    #Prompt the users for their name and dream location
    name = input('What is your name?: ')
    response = input("What is your dream vacation location?: ")

    #Store the responses in a dictionary 
    responses[name] = response

    #Find out if anyone else is taking the poll
    repeat = input("Would you like another person to respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#Polling is complete. show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to travel to {response}\n")










