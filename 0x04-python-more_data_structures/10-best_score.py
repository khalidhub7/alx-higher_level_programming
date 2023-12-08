#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    value = 0
    key = None
    for i, j in a_dictionary.items():
        if j > value:
            value = j
            key = i
    return key
