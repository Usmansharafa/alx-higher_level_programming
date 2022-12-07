#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return None
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
