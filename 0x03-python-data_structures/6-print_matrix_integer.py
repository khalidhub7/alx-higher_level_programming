#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if (len(i)) == 0:
            print()
        for x in range(len(i)):
            print("{:d}".format(i[x]), end="\n" if x is len(i) - 1 else " ")
