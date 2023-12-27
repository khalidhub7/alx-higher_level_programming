#!/usr/bin/python3
"""my class"""


class Square:
    """define square"""
    def __init__(self, size=0):
        """define raises"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """return squared of size"""
        return self.__size ** 2
