#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix[0]:
        return
    new_matrix = []
    for i in range(len(matrix)):
        inner_matrix = list(map(lambda x: x ** 2, matrix[i]))
        new_matrix.append(inner_matrix)
    return new_matrix
