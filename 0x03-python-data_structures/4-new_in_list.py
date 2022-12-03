#!/usr/bin/python3
"""
    Replaces an element in a list at a specific position without modifying
    original list

    Return:
        modified copy of original list if successful
"""


def new_in_list(my_list, idx, element):
    if not my_list:
        return
    new_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    new_list[idx] = element
    return new_list
