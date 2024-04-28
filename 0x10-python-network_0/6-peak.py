#!/usr/bin/python3


""" find a peak in a list """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    elif len (list_of_integers) != 0:
        list_of_integers.sort()
        list_of_integers.reverse()
        return (list_of_integers[0])
