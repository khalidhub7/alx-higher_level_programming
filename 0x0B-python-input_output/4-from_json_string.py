#!/usr/bin/python3
'''my module'''


import json


def from_json_string(my_str):
    '''change json to python string'''
    return json.loads(my_str)
