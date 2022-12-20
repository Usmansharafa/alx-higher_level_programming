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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size, end='')
                print()
