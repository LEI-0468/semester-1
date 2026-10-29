# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self,x_coordinate,y_coordinate):
        self.x=x_coordinate
        self.y=y_coordinate
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x,self.y)
    def distance_to(self):
        pass
    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
