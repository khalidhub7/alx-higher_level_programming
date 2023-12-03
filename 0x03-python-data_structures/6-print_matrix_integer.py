#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix[0][:2]:
        print("{:d}".format(i), end=" ")
    print(matrix[0][2], end="$\n")
    for j in matrix[1][:2]:
        print("{:d}".format(j), end=" ")
    print(matrix[1][2], end="$\n")
    for x in matrix[2][:2]:
        print("{:d}".format(x), end=" ")
    print(matrix[2][2], end="$\n")
    print("--$\n$")
