#!/usr/bin/python3
class Rectangle:

    """ An empty class that defines a rectangle """
    instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.instances += 1

    @property
    def width(self):
        """ Method that the gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that the sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0 ")

        self.__width = value

    @property
    def height(self):
        """ Method that the gets the heights of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that the sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0 ")

        self.__height = value

    def area(self):
        """ Public instance that returns the area of the rectangle
        """
        return int(self.width) * int(self.height)

    def perimeter(self):
        """ Method that the returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0

        return (int(self.width) * 2) + (int(self.height) * 2)

    def __str__(self):
        """ Method that returns the Rectangle #
        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string representation of the instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """
        Rectangle.instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method returns big rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2