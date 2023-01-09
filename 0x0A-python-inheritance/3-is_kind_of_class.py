#!/usr/bin/python3
"""Module that defines a function that checks if an object is an instance of a
class or of a class that inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is an instance of a class or of a
    class that inherited from the specified class

    Args:
        obj (any): object to be checked
        a_class (type): the class to match the type of obj to
    Returns:
        True if obj is an instance of either the specified class or a
        class that inherited from the specified class.
        Otherwise, False
    """
    return isinstance(obj, a_class)
