#!/usr/bin/python3
"""write w appand"""

def append_after(filename="", search_string="", new_string=""):
    '''append str for specifique search str'''
    with open(filename, "r", encoding='UTF8') as a:
        b = a.readlines()
        c = []
        c.append(b)
        for i in c:
            if i == search_string:
                i += new_string
    with open(filename, 'w', encoding='UTF8') as x:
        z = x.write(c)
        return z
