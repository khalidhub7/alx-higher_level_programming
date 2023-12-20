#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    g = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            g += 1
        except(ValueError, TypeError):
            pass
        i += 1
        return g
