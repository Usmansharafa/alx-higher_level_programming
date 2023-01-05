#!/usr/bin/python3
""""Module to print first name and last name"""


def say_my_name(first_name, last_name=""):
    """"Prints first and last name

    Args:
        first_name (str): first_name to be printed
        last_name (str): last_name to be printed

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
