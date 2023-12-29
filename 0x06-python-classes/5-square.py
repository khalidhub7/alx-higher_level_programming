#!/usr/bin/python3
"""define square"""


class Square:
    """inialization """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ get w set w raises"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """define squared"""
        return self.__size ** 2

    def my_print(self):
        """define print function"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
