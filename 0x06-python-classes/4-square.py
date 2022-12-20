#!/usr/bin/python3
"""OOP Python."""


class Square:
    """"Class representing a square."""

    def __init__(self, size=0):
        """Initializing a class.

        Args:
            size (int): size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """int: size of square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area module

        Returns:
            int: square of size of square
        """
        return self.__size ** 2
