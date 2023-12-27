#!/usr/bin/python3
"""my class"""


class Square:
    """square define"""
    def __init__(self, size=0):
        """self function """
        self.size = size
    @property
    def size(self):
        """getter function"""
        return self.__size
    @size.setter
    def size(self, value):
        """ setter funcion """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    def area(self):
        """ squared funcion"""
        return self.size ** 2
