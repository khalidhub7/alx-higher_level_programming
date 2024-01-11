#!/usr/bin/python3
'''my module'''


def read_file(filename=""):
    '''read a file'''

    with open(filename, "r", encoding="UTF8") as a:
        print(a.read(), end="")
