#!/usr/bin/python3
"""Module that defines a class with a method that prints a sorted list"""


class MyList(list):
    """Class representing MyList"""
    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        print(sorted(self))
