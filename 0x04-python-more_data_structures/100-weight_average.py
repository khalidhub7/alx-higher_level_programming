#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    su = 0
    for i in my_list:
        j = i[0] * i[1]
        su += j
        l = 0
    for z in my_list:
        l += z[1]
    b = su / l
    return b
