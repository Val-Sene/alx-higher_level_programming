#!/usr/bin/python3
"""


A class rectangle defined


"""


class Rectangle:

    """ An empty class that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string representation of the instance
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """
        print("Bye rectangle...")
