#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    '''append str for specifique search str'''
    with open(filename, "w", encoding='UTF8') as a:
        for search_string in a:
            return search_string + new_string
