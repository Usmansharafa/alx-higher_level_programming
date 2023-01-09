#!/usr/bin/python3
"""Module that defines a class with a method that prints a sorted list"""


class MyList(list):
    """Class representing MyList"""
    
    def __init__(self):
        """Initializes a new list"""
        super().__init__()

    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        print(sorted(self))
