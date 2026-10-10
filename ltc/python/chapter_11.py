#Testing your code - Tyr it yourself 11.3: Employee

class Employee:
    """Model an employee"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary 


    def give_raise(self, increase=5000):
        self.salary += increase 
        return self.salary 
    

employ = Employee('Olamide', 'Olubode', 10000)
print(employ.give_raise(2000))

