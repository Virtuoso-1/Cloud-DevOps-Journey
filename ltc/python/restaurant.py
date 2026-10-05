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
