from random import randint
# x = randint(1, 6)
# print(x)

class Die:
    """Modelling a Die"""
    def __init__(self, sides=6):
        """initializing die attributes"""
        self.sides = sides
        
    def roll_die(self):
        """Rolls a die"""
        side = randint(1,self.sides)
        print(side)
        

small_die = Die()
medium_die = Die(10)
large_die = Die(20)

for i in range(10):
    small_die.roll_die()
print("")
for i in range(10):
    medium_die.roll_die()
print("")
for i in range(10):
    large_die.roll_die()
