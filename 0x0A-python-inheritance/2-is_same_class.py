#!/usr/bin/python3
"""my module"""


def is_same_class(obj, a_class):
    """check if obj is in some class"""
    if type(obj) == a_class:
        return True
    else:
        return False
