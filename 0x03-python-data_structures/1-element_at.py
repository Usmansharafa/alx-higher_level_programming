#!/usr/bin/python3
"""
    Retrieves element from a list

    Return:
    Element in list
"""


def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]
