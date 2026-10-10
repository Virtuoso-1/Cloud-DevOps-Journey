"""This script keeps various code from different chapter for the purpose of a 
quick and short test."""

#Importing User class from the module.py
from module import User

new_user = User('Mike', 'Alonge', '45', '60')
new_user.describe_user()
print("\n")

#importing Admin1 from module.py 
from module import Admin1

user = Admin1('Kunle', 'Makinde', '40', '35')
user.privileges.show_privileges()
print("\n")

#Importing multiple classes from a module 
from module import Car, Battery, ElectricCar

new_car = Car('Nissan', 'Mustang', 2004)
print(new_car.get_descriptive_name())
print("\n")


#Try it yourself 9.10 to 9.12 
from restaurant import Restaurant

new_canteen = Restaurant('Yakoyo', 'Amala')
new_canteen.describe_restaurant()
print("\n")


#9.11 - Imported Admin
from module import *

office_admin = Admin1('Mary', 'Dada', 27, 80)
office_admin.privileges.show_privileges()
print("\n")



