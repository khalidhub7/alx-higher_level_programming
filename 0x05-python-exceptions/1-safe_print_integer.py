#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = print("{:d}".format(value))
        return x ,True
    except ValueError:
        return False
