#!/usr/bin/python3
"""Module creating a Base Geometry class"""


class BaseGeometry():
    """A class representing base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer

        Args:
            name (str): The name of the parameter
            vlaue (int): The parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
