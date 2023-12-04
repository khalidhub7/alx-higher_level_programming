#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix[0][:2]:
        print(i, end=" ")
    print(matrix[0][2])
    for i in matrix[1][:2]:
        print(i, end=" ")
    print(matrix[1][2])
    for i in matrix[2][:2]:
        print(i, end=" ")
    print(matrix[2][2])
