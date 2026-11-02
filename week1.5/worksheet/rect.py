# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance( height,int):
            raise TypeError("the parameter should be int")
        if not isinstance( width,int):
            raise TypeError("the parameter should be int")
        if (width <= 0 ):
            raise ValueError("the parameter should >0")
        if (height <=0) :
            raise ValueError("the parameter should >0")
        self.width = width
        self.height = height
    # Implement methods is_square(), area() & perimeter() here
    def is_square(self): 
        """
            detect the rectangle is a square or not
        """
        if self.width == self.height: return True 
        else: return False
    def area(self):
        """
        Returns the area of the rectangle.
        """
        ans = self.width*self.height
        return ans # calculate the area
    def perimeter(self):
        """
        calculate the perimeter
        """
        ans = self.width*2 + self.height*2
        return ans 
    # (See README.md for details of what they should do)


