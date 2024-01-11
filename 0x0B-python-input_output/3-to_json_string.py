#!/usr/bin/python3
'''my module'''


import json


def to_json_string(my_obj):
    '''return json string'''
    with open(my_obj, "r", encoding='UTF8') as a:
        return json.dumps(a)
