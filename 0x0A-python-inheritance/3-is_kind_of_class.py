#!/usr/bin/python3
"""my module"""


def is_kind_of_class(obj, a_class):
    """check if is instance of
    and or if  the object is an instance of a class that inherited from"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
