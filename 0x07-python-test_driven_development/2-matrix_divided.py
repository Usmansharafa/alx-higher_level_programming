#!/usr/bin/python3
"""Module to divide the elements of a matrix by a number"""


def matrix_divided(matrix, div):
    """Function to divide the elements of a matrix by a divisor

    Args:
        matrix (list of list): 2-dimensional list
        div (int/foat): Divisor

    Raises:
        TypeError: if matrix is not a matrix of integers/floats
        TypeError: if rows of matrix are not of equal length
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0

    Return:
        Matrix consisting of the result of the division of each element by div
    """

    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    msg_3 = "div must be a number"
    msg_4 = "division by zero"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(msg_1)
    for row in matrix:
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(msg_1)
    if not (all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError(msg_2)
    if not(isinstance(div, int) or isinstance(div, float)):
        raise TypeError(msg_3)
    if div == 0:
        raise ZeroDivisionError(msg_4)
    new = [[round(num / div, 2) for num in row] for row in matrix]
    return new
