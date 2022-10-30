#!/usr/bin/python3
""" A module for class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Intializes the class instance """
        super().__init__(size, size, x, y, id)

