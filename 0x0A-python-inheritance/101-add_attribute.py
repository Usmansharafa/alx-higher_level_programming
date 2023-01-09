#!/usr/bin/python3
"""Module that defines a function that adds an attribute to objects"""


def add_attribute(obj, att, value):
    """Adds an attribute to an object if possible

    Args:
        obj (any): the object to add an attribute to
        att (str): attribute to be added
        value (any): value of att
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
