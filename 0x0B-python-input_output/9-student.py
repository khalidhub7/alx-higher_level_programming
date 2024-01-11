#!/usr/bin/python3
'''my module'''


class Student:
    '''class'''

    def __init__(self, first_name, last_name, age):
        '''initia'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return dict of student'''
        return self.__dict__
