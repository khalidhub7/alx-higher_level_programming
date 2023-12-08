#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_2 = dict(a_dictionary)
    for i in dic_2:
        dic_2[i] = dic_2[i] * 2
    return (dic_2)
