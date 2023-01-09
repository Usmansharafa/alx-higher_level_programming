#!/usr/bin/python3
"""Module defining a Rectangle class that inherits from
BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
