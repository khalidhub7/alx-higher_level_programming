#!/usr/bin/python3
'''my module'''


import json


def save_to_json_file(my_obj, filename):
    '''JSON representation'''
    with open(filename, 'w', encoding='UTF8') as a:
        b = json.dumps(my_obj)
        a.write(b)
