"""This Module contains the Die class for modelling a die"""
from random import randint

class Die:
    """This class models a die"""
    def __init__(self, nsides=6):
        """Initializing die attributes"""
        self.nsides = nsides
        
    def roll(self):
        """Return a number roll"""
        return randint(1, self.nsides)
    
if __name__ == "__main__":
    print('wher'*0)
    