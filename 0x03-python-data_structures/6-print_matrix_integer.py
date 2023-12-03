#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) == 0:
            print()
        for j in range(len(i)):
            print("{}".format(i[i]), end="\n" if j is len(i) - 1 else " ")
