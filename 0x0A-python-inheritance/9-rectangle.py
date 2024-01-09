#!/usr/bin/python3
'''module'''


class BaseGeometry:
    '''class'''
    def area(self):
        '''define area'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''validate value'''
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
        value = value
class Rectangle(BaseGeometry):
    '''class'''
    def __init__(self, width, height):
        '''initialization'''
        super().integer_validator("w", width)
        super().integer_validator("h", height)
        self.__width = width
        self.__height = height
    def area(self):
        '''calcul area'''
        return self.__height * self.__width
    def __str__(self):
        '''print method'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
