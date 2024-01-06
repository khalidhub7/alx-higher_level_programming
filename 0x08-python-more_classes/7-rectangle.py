#!/usr/bin/python3
"""define a Rectangle class"""


class Rectangle:
    """my empty class"""

    number_of_instances = 0
    """calcul instances"""
    
    print_symbol = '#'
    """print with specifiq symbole"""

    def __init__(self, width=0, height=0):
        """define instances"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get dyal width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set dyal width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get dyal height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set d height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area"""
        return self.width * self.height

    def perimeter(self):
        """ return perimeter"""
        p = 0
        if self.height == 0 or self.width == 0:
            return p
        p = 2 * (self.width + self.height)
        return p

    def __str__(self):
        """ return # type"""
        gg = ""
        if self.__height != 0 and self.__width != 0:
            gg += '\n'.join(str(self.print_symbol) * self.__width for i in range(self.__height))
        return gg

    def __repr__(self):
        """ repr methode """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete methode"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
