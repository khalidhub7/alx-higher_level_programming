#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    gg = 0
    try:
        while gg is not x:
            print(my_list[gg], end="")
            gg += 1
    except IndexError:
        None
    print()
    return gg
