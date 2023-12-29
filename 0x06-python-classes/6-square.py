#!/usr/bin/python3
"""define square"""


class Square:
    """inialization """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ get w set w raises"""
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        for i in value:
            if i < 0 or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """define squared"""
        return self.__size ** 2

    def my_print(self):
        """define print function"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
