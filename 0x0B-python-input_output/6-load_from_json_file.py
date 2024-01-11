#!/usr/bin/python3
'''my module'''


import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”'''
    with open(filename, "r", encoding='UTF8') as a:
        b = json.loads(a)
        return b
