#!/usr/bin/python3


""" find a peak in a list """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    elif len (list_of_integers) != 0:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i:
                if i > peak:
                    peak = i
        return peak
