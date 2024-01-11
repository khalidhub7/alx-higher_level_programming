#!/usr/bin/python3
'''my module'''


import sys
import json


def class_to_json(obj):
    '''dict of obj'''
    return obj.__dict__
