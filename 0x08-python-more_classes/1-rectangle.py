#!/usr/bin/python3
"""define a Rectangle class"""


class Rectangle:
    """my empty class"""
    def __init__(self, width=0, height=0):
        """define instances"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """get && set dyal width"""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    @property
    def height(self):
        """get && set dyal height"""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
