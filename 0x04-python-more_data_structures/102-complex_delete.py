#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary):
        if value == a_dictionary[i]:
            key = i
            del a_dictionary[key]
    return a_dictionary
