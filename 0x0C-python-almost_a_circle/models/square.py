#!/usr/bin/python3
""" A module for class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Intializes the class instance """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """ Getting the size value """
        return self.width

    @size.setter
    def size(self, value):
        """ Setting the size value """
        self.width = value
        self.height = value
        
    def __str__(self):
        """ Displays a formated string of the square """
        first_part = "[Square] "
        second_part = "({}) ".format(self.id)
        third_part = "{}/{} - ".format(self.x, self.y)
        fourth_part = "{}/{}".format(self.width, self.height)

        return first_part+ second_part+ third_part+ fourth_part
    
    def __str__(self):
        """ A special string method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    
   
