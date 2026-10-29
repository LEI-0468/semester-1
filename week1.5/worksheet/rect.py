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
        if not isinstance((width,height),int):
            TypeError("the parameter should be int")
        if (width or height) <=0:
                    ValueError("the parameter should >0")
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
        return self.width*self.height# calculate the area
    def perimeter(self):
        return self.width*2 + self.height # calculate the perimeter
    # (See README.md for details of what they should do)


