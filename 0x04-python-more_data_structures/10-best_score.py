#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    gg = 0
    elif a_dictionary not None:
        gg = max(a_dictionary, key=lambda x: a_dictionary[x])
        return (gg)
