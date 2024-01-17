#!/usr/bin/python3
'''base module.'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class.'''

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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''get / set'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '''get / set'''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '''get / set'''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '''area of rectangle'''
        return self.__height * self.__width

    def display(self):
        '''1--print width && height in # symbole
        2-- update by taking care of x and y
        '''
        str_updated = '\n' * self.y + \
                      (' ' * self.x + '#' * self.width + '\n') * self.height
        print(str_updated, end='')

    def __str__(self):
        '''Return string info to the user.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(self.__class__.__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''update helper'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update function'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
