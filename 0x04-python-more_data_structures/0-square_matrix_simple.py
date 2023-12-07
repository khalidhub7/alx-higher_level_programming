#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for raw in matrix:
        elem = []
        for i in raw:
            squar_elem = i ** 2
            elem.append(squar_elem)
        squared.append(elem)
    return (squared)
