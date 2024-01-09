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
