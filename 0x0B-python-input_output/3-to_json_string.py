#!/usr/bin/python3
import json
'''my module'''


def to_json_string(my_obj):
    '''return json string'''
    b =""
    with open(my_obj, "r", encoding='UTF8') as a:
        json.dumps(a, b)
        return b
