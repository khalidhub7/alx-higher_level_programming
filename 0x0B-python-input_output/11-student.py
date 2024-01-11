#!/usr/bin/python3
'''my module'''


class Student:
    '''class'''
    def __init__(self, first_name, last_name, age):
        '''initia'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return dict of student'''
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        m = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                m[k] = v
        return m

    def reload_from_json(self, json):
        '''replace dict'''
        for i, j in json.items():
            if i in self.__dict__:
                self.__doc__[i] = j
