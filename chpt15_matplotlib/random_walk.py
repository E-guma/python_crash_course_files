from random import choice

class RandomWalk:
    """ A class to generate random walks"""
    
    def __init__(self, npoints=5000):
        """initialize walk attributes"""
        self.npoints = npoints
        # initialize walk lists at 0,0
        self.x_pos = [0]
        self.y_pos = [0]
        self.fill_walk_list()

    def fill_walk_list(self):
        """generate random decions for walk path"""
        while len(self.x_pos) < self.npoints:
            # Take step in the x direction
            x_step = self.get_step()
            # Take step in the y direction
            y_step = self.get_step()
            # Remove null steps
            if x_step == 0 and y_step == 0:
                continue
            # Get new positons
            new_x = self.x_pos[-1] + x_step
            new_y = self.y_pos[-1] + y_step
            # Append new positions
            self.x_pos.append(new_x)
            self.y_pos.append(new_y)
                         
    def get_step(self):
        """return next step and direction"""
        dirct = choice([-1,1])
        dis = choice(list(range(5)))
        return dis * dirct
