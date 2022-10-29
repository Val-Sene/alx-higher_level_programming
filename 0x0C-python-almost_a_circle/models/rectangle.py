#!/usr/bin/python3
""" Module for class Rectangle """


from base import Base


class Rectangle(Base):
    """ A rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Intializes the class instances """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getting the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width value """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getting the height value """
        return self.___height

    @height.setter
    def height(self, value):
        """ Setting the height value """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    @property
    def x(self):
        """ Getting the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting the x value """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")

        self.__x = value

    @property
    def y(self):
        """ Getting the y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting the y value """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__y = value
