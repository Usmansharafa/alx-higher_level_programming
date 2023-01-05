#!/usr/bin/python3
"""Module to print square using '#' character"""


def print_square(size):
    """Function that prints a square using '#' character of size 'size'.

    Args:
        size (int/float): size of square to be printed

    Raises:
        TypeError: if size is not an integer or float
        ValueError: if size is less than zero
    """

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        for i in range(int(size)):
            for j in range(int(size)):
                print("#" * int(size), end='')
            print()
