#!/usr/bin/python3
"""
    Removes all characters c and C from a string
"""


def no_c(my_string):
    new_string = [char for char in my_string if char not in "cC"]
    return "".join(new_string)
