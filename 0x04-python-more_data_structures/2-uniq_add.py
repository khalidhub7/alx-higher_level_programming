#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    b = 0
    for i in a:
        b += i
    return b
