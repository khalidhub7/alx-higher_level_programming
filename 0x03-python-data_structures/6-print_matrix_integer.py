def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row[:-1]:
            print("{:d}".format(element), end=" ")
        print("{:d}$".format(row[-1]))
    print("--$\n$")
