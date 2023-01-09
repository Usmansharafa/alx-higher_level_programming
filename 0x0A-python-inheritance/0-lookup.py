#!/usr/bin/python3
"""Module that defines a funtion that returns a list of available attributes
and methods of an object"""


def lookup(obj):
    """FUnction that returns the list of available attributes and methods of
    an object"""
    return dir(obj)
