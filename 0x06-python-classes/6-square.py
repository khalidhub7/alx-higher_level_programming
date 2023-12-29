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
        """get/set dyal position"""
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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """define squared"""
        return self.__size ** 2

    def my_print(self):
        """define print function"""
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            print("_" * self.__position[0], end="")
            print("#" * self.size)
