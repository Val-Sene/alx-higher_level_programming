#!/usr/bin/python3
def lookup(obj):
    """ Function that returns the number of attributes
        and methods

    Args:
        obj: instance of the class

    Returns:
        List of attributes and methods
    """

    return dir(obj)
