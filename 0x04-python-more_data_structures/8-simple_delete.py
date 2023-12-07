#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    remove_key = key
    if remove_key in a_dictionary:
        del a_dictionary[remove_key]
    return a_dictionary
