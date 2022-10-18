#!/usr/bin/python3
""" A module to add two numbers """


def add_integer(a, b=98):
    """ Function that adds two integer/float numbers to
    
    Args:
        a: first number to be summed
        b: second number to be summed to
        
    returns:
            The sum of the two numbers
            
    raises:     
            TypeError: If a or b are not integer and/or float numbers 
                
    """
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
