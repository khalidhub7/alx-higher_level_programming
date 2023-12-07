#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my = []
    for i in my_list:
        if i == search:
            i = replace
            my.append(i)
        elif i != search:
            my.append(i)
    return my
