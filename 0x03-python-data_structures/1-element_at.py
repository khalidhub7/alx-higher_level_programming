#!/usr/bin/python3
def element_at(my_list, idx):
    from my_list import idx
    if idx < 0 or idx != range(my_list):
        return None
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))