#!/usr/bin/python3
"""Module that defines a function that checks whether an object is an instance
of a class that inherited from a specified class"""


def inherits_from(obj, a_class):
    """Function that checks whether an object is an instance of a class that
    inherited from a specified class

    Args:
        obj (any): object to be checked
        a_class (type): the class to match the type of obj to
    Returns:
        True if obj is an instance of a class that inherited from a_class
        Otherwise, False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
