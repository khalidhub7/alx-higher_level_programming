#!/usr/bin/python3
"""find peeak number in a list"""


def find_peak(list_of_integers):
    """peak"""
    if not list_of_integers:
        return None

    for i in range(1, (len(list_of_integers) - 1)):
        try:
            current_element = list_of_integers[i]
            left_value = list_of_integers[i - 1]
            right_value = list_of_integers[i + 1]
        except IndexError:
            pass
        if current_element >= left_value and current_element >= right_value:
            return current_element
