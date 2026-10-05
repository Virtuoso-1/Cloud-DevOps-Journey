#Classes 
#Try it yourself - 9.1 to 9.3 - Restaurant
class Restaurant:
    """A simple attempt to model a Restaurant"""

    def __init__(self, name, cuisine_type):
        """Initializing the attributes to model a restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describing the restarant and cusisine type it serves"""
        print(f"{self.name} serves {self.cuisine_type} on mondays.")

    def open_restaurant(self):
        """Print a message that the restaurant is open"""
        print(f"{self.name} is open to take your orders!")


restaurant = Restaurant('KFC', 'Chiken-pie')
print(f"The name of the Restaurant is {restaurant.name}")


#9.2 - Three Restaurants
restaurant2 = Restaurant('Domino', 'Pizza')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant.open_restaurant()


#9.3 - Users 
class User:
    """A simple class that models a user"""

    def __init__(self, first_name, last_name, age, bmi):
        """Initialize attribute to make a person"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bmi = bmi

    def describe_user(self):
        """Return a neatly formatted details of the user"""
        print(f"User details:\nFullname:{self.first_name} {self.last_name}\n"
              f"age: {self.age}\n"
              f"bmi: {self.bmi}")

    def greet_user(self):
        """Greet the user with their fullname"""
        print(f"Welcome to Yellow Amber, {self.first_name.title()} {self.last_name.title()}! ")


user1 = User('olamide', 'olubode', '24', '45')
user2 = User('isaac', 'ejemudaro', '25', '50')

print(f"\n The fullname of the user1 is: {user1.first_name} {user1.last_name}\n")
    
user1.describe_user()
user2.greet_user()


"""Working with Classes & Instances"""
#Try it yourself - 9.4 - Number Served
class Restaurant:
    """A simple attempt to model a Restaurant"""

    def __init__(self, name, cuisine_type):
        """Initializing the attributes to model a restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describing the restarant and cusisine type it serves"""
        print(f"{self.name} serves {self.cuisine_type} on mondays.")

    def open_restaurant(self):
        """Print a message that the restaurant is open"""
        print(f"{self.name} is open to take your orders!")

    def set_number_served(self, number):
        """To set the number of customer that has been served"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't the number lower than previous value.")

    def increment_number_served(self, increase):
        """To increase the number of the customer served"""
        self.number_served += increase


#Creating an intance of the clas restaurant
restaurant3 = Restaurant('Coldstone', 'Fries')
print(f"This is the no of the customers served: {restaurant3.number_served}\n")


#Changin the value of the number served
restaurant3.number_served = 45
print(f"This is the no of the customers served: {restaurant3.number_served}")


#Calling the nw methods on the  previous instances 
restaurant3.set_number_served(40)
print(f"This is the no of the customers served: {restaurant3.number_served}")

restaurant3.set_number_served(50)
print(f"This is the no of the customers served: {restaurant3.number_served}")

restaurant3.increment_number_served(25)
print(f"This is the no of the customers served: {restaurant3.number_served}\n")


#9.5 - Login Attempts 
class User:
    """A simple class that models a user"""

    def __init__(self, first_name, last_name, age, bmi):
        """Initialize attribute to make a person"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bmi = bmi
        self.login_attempts = 0

    def describe_user(self):
        """Return a neatly formatted details of the user"""
        print(f"User details:\nFullname:{self.first_name} {self.last_name}\n"
              f"age: {self.age}\n"
              f"bmi: {self.bmi}")

    def greet_user(self):
        """Greet the user with their fullname"""
        print(f"Welcome to Yellow Amber, {self.first_name.title()} {self.last_name.title()}! ")

    def increment_login_attempts(self):
        """To increase the number of times a user attempts to login"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset the value of login attempts to zero"""
        self.login_attempts = 0

#Creating an instance of the class User
user3 = User('James', 'Bond', '66', '40')
user3.describe_user()

user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f"The current login attempts of this user is: {user3.login_attempts}\n")

user3.reset_login_attempts()
print(f"The reset value: {user3.login_attempts}\n")



"""Inheritance """
#Try it youeself 9.6 to 9.9 - Ice Cream Stand
class IceCreamStand(Restaurant):
    """A subcalss that inherits from the superclass Restaurant; to model 
    a simple icecream stand"""
    def __init__(self, name, cuisine_type):
        """Initialize the attributes of the parent class"""
        super().__init__(name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']

    def display_flavors(self):
        """Display the flavours available at the stand"""
        print(f"These are the available flavors at the stand right now: ")
        for flavor in self.flavors:
            print(f"{flavor}")


#Creating an instance of the class Icecreamstand
stand1 = IceCreamStand('Coldstone', 'Icrecrem')
stand1.display_flavors()

        
#9.7 - Admin 
class Admin(User):
    """An admin class that inherit from User"""
    def __init__(self, first_name, last_name, age, bmi):
        super().__init__(first_name, last_name, age, bmi)
        """Adding extra attribute: privilege that stores list of strings"""
        self.privilege = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the administrator's set of privieges"""
        print("These are the list of administrator's privileges: ")
        for privilege in self.privilege:
            print(privilege)


admin1 = Admin('Seun', 'Olubode', '27','30')
admin1.show_privileges()
print("\n")


#9.8 - Privileges 
class Privileges:
    """A simple class that display the list of an administrator's privilege"""
    def __init__(self):
        self.privilege = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
            """Display the administrator's set of privieges"""
            print("These are the list of administrator's privileges: ")
            for privilege in self.privilege:
                print(privilege)


class Admin1(User):
    """An admin class that inherit from User"""
    def __init__(self, first_name, last_name, age, bmi):
        super().__init__(first_name, last_name, age, bmi)
        self.privilege = Privileges()


admin_pure = Admin1('James', 'Bond', '57', '28')
admin_pure.privilege.show_privileges()
print("\n")

#9.9 - Battery Upgrade 
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
 
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
 
 
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
 
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:    
            range = 255
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery = 65
        else:
            print("Already has the expected size")

    


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.Then initialize attributes 
        specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()


car_1 = ElectricCar('Toyota', 'Camry', '2026')
car_1.battery.get_range()
print("\n")



#Python Standard library - Try it yourself 9.13 to 9.16
from random import randint

class Die:
    """A simple class that models a rolling die"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die_6 = Die()
i = 0 
die_rolling_10 = []

while i < 10:
    roll = die_6.roll_die()
    die_rolling_10.append(roll)
    i += 1

print(f"\nRandom rolling of a 6-sided die 10 times: {die_rolling_10}")

die_10 = Die(10)
i = 0 
die_rolling_20 = []

while i < 20:
    roll = die_10.roll_die()
    die_rolling_20.append(roll)
    i += 1

print(f"\nRandom rolling of a 10-sided die 20 times: {die_rolling_20}\n")


#9.14 Lottery 
series_num_and_letter = (2, 6, 4, 3, 't', 'y', 'w', 's', 'h', 'x', 10)

from random import choice

i = 0
while i < 4:
    lottery = choice(series_num_and_letter)
    print(lottery)
    i += 1

    if lottery == 4:
        print("You ticket matches the expected number 4, you won the prize")
    else:
        print("Input $5 coin and try your luck again\n") 


#9.15 - Lottery Analysis 
my_ticket = (2, 6, 4, 3, 't', 'y', 'w', 's', 'h', 'x', 10)
polling_number = True

while polling_number:
    lottery = choice(my_ticket)
    print(lottery)

    if lottery == 10:
        print("You have won the prize")
        polling_number = False
    else:
        print("Continue running the number until your ticket wins")





      


