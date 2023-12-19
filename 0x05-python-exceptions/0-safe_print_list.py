#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            if i <= my_list[x - 1]:
                print(i, end="")
        print()
        return x
        except IndexError:
            len = 0
            for i in my_list:
                len += 1
                print(i, end="")
            print()
            return len
