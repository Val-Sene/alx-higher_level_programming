#!/usr/bin/python3
""" Module for class Rectangle """


from models.base import Base


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
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getting the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height value """
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Getting the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting the x value """
        if not isinstance(int, value):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Getting the y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting the y value """
        if not isinstance(int, value):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Method returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ Method that prints a # rectangle according
        to the size of width and height value
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ Displays a formated string of the rectangle """
        first_part = "[Rectangle] "
        second_part = "({}) ".format(self.id)
        third_part = "{}/{} - ".format(self.x, self.y)
        fourth_part = "{}/{}".format(self.width, self.height)

        return first_part+ second_part+ third_part+ fourth_part

    def update(self, *args, **kwargs):
        """ Method takes both keyword/non-keyword arguments """
        if args != None and len(args) != 0:
            attribute_list = ['id','width', 'height', 'x','y']
            for i in range(len(args)):
                setattr(self, attribute_list[i], args[i])
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
