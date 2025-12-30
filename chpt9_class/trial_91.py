# Class of Restaurants
class Servings:
    """Managing record of number of served customers"""
    def __init__(self, number_served=0):
        """initialize number served attribute"""
        self.number_served = number_served
        
    def show_served(self):
        """Shows the number of customers served so far"""
        print(f"We've served {self.number_served} customers so far")
        
    def set_number_served(self, served):
        """Can reset the number of number of customers served to any value"""
        if served >= self.number_served:
            self.number_served = served
            
    def increment_number_served(self,just_served=None):
        """Increases the number of customers served by any positive amount or by one"""
        if just_served and just_served >= 0:
            self.number_served += just_served
        else:
            self.number_served += 1

        
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.customers_served = Servings()

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.name.title()} serves wonderful {self.cuisine_type} cuisine.\n")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.name.title()} is now open!\n") 
        
    
class IceCreamStand(Restaurant):
    """Modelling an ice cream stand"""
    def __init__(self, name, cuisine_type=None):
        """initializing super class attributes"""
        super().__init__(name, cuisine_type)
        """initialize instance attributes"""
        self.flavours = ['vanilla', 'chocalate', 'strawberry']
        
    def display_flavours(self):
        """Displays the list of ice cream flavours"""
        print('List Of Ice Cream Flavours:')
        for i, flavour in enumerate(self.flavours, start=1):
            print(f'{i}. {flavour.title()}')
    
my_restaurant = Restaurant('foodies mix','italian')
print(my_restaurant.name)
my_ice_cream_stand = IceCreamStand('G-Sweets', 'ice cream')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavours()
my_ice_cream_stand.customers_served.show_served()
my_ice_cream_stand.customers_served.increment_number_served(5)
my_ice_cream_stand.customers_served.show_served()

    