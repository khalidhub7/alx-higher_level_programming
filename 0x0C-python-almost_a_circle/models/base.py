#!/usr/bin/python3
'''base module.'''
from json import dumps, loads


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
        '''write JSON str of 'list_objs' to a file'''
        myfile = '{}.json'.format(cls.__name__)
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(myfile, 'w', encoding='UTF-8') as a:
            a.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        '''return json str'''
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''loads instance from dictionary'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
