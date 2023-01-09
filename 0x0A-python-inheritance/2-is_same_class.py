#!/usr/bin/python3
"""Module that defines a function that checks whether an object is exactly an
instance of a specific class"""


def is_same_class(obj, a_class):
    """Function that checks whether an object is exactly an instance of a
    specific class

    Args:
        obj (any): object to check
        a_class (type): the class to match the type of obj to
    Returns:
        True if obj is exactly an instance of a_class, else
        False
    """
    return type(obj) == a_class
