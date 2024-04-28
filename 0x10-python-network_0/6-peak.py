#!/usr/bin/python3

"""Find a peak in a list."""

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i

    return peak
