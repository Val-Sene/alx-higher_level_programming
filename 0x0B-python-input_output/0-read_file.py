#!/usr/bin/python3
"""
  Module that contains a function to read all contents of a file
"""


def read_file(filename=""):
    """ Function that reads contents of a text file

    Args:
        filename: Name of the file

    Raises:
        Exception: When file cannot open
  """


with open("filename", "r", encoding="utf-8") as file:
    print(file.read(), end='')
