#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    remove_key = key
    if remove_key in a_dictionary:
        a_dictionary.pop(remove_key)
        print(a_dictionary)
