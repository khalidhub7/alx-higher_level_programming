#!/usr/bin/python3
'''my module'''


def append_write(filename="", text=""):
    '''append function'''
    with open(filename, "a", encoding='UTF8') as a:
        return (a.write(text))
