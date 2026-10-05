"""This script keeps various code from different chapter for the purpose of a 
quick and short test."""

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



#9.8 - Privileges
class Privileges:
    """A simple class that display the list of an administrator's privilege"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
            """Display the administrator's set of privieges"""
            print("These are the list of administrator's privileges: ")
            for privilege in self.privileges:
                print(privilege)


class Admin1(User):
    """An admin class that inherit from User"""
    def __init__(self, first_name, last_name, age, bmi):
        super().__init__(first_name, last_name, age, bmi)
        self.privileges = Privileges()



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

