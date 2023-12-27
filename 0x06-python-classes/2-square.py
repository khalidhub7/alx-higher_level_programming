#!/usr/bin/python3
"""my class in python."""
class Square:
    """def square hhh """
    def __init__(self, size = 0):
        self.__size = size
    @property
    def size(self, size):
        if size == int:
            return self.__size
        if size < 0:
            raise ValueError("size must be >= 0")
        raise TypeError("size must be an integer")
