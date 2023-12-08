#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = []
    for i in my_list:
        i = i * number
        new.append(i)
    return (new)
