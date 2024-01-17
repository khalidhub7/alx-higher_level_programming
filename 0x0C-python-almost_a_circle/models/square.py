#!/usr/bin/python3
''' square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''the square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return string info to the user about square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''setup size of square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
