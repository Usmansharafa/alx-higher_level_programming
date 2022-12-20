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

    def my_print(self):
        """my_print module

        Prints in stdout the square with the '#' character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, end='')
                print()
