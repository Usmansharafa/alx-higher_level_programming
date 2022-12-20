#!/usr/bin/python3
"""OOP Python."""


class Square:
    """"Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a class.

        Args:
            size (int): size of a square.
            position (tuple): coordinates of a square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """tuple: coordinate of square.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end='') for j in range(self.__position[0])]
                [print("#", end='')for k in range(self.__size)]
                print()
