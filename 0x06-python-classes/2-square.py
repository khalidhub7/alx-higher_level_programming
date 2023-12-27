#!/usr/bin/python3
"""my class in python."""
class Square:
    """def square hhh """
    def __init__(self, size=0):
        """define exception"""
        if type(size) == str:
            raise TypeError('size must be an integer')
        elif type(size) != str:
            if size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size
