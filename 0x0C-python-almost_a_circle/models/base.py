#!/usr/bin/python3
'''base module.'''
import json


class Base:
    '''class.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''return json string'''
        a = json.dumps(list_dictionaries)
        return a
