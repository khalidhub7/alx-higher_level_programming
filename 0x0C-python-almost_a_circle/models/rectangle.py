#!/usr/bin/python3
'''base module.'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get / set'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''get / set'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''get / set'''
        return self.__x

    @height.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''get / set'''
        return self.__y

    @height.setter
    def y(self, value):
        self.__y = value
