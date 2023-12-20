#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    gg = True
    try:
        print("{:d}".format(value))
    except Exception as ee:
        print("Exception:", ee, file=sys.stderr)
        gg = False
    return gg
