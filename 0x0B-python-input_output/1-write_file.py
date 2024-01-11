#!/usr/bin/python3
'''my module'''


def write_file(filename="", text=""):
    '''write in file'''

    with open(filename, "w", encoding= "UTF8") as a:
        return (a.write(text))
