#!/usr/bin/python3
"""my module"""


def inherits_from(obj, a_class):
    """if obj in class and
    obj != type a_class
    check task 4 for more detail"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
