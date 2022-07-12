#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for integer in matrix:
        print()
        for i in integer:
            if count == (len(integer) - 1):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".fromat(i), end=" ")
            count += 1
        print("")
