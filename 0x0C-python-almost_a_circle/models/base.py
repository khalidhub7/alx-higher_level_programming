#!/usr/bin/python3
'''base module.'''
from json import dumps


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return json string'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''''''
        myfile = "{}.json".format(cls.__name__)
        if list_objs is None or not list_objs:
            with open(myfile, 'w') as a:
                a.write('[]')
        else:
            with open(myfile, "w") as b:
                b.write(dumps(list_objs))
