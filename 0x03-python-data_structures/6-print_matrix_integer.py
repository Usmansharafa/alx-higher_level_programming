#!/usr/bin/python3
"""
    Prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    else:
        for row in matrix:
            i = 0
            for col in row:
                i += 1
                if i != 3:
                    print("{:d} ".format(col), end="")
                else:
                    print("{:d}".format(col))
