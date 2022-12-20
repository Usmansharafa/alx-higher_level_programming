#!/usr/bin/python3
"""OOP Python."""


class Square:
    """"Class representing a square."""

    def __init__(self, size=0):
        """Initializing a class.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area module

        Returns:
            int: square of size of square.
        """
        return self.__size ** 2
