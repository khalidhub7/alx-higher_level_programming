#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = sorted(a_dictionary.keys())
    for i in b:
        print("{}: {}".format(i, a_dictionary[i]))
