#!/usr/bin/python3
""""Module to add two integers"""


def add_integer(a, b=98):
    """Adds two integers and returns the result of the addition

    Args:
        a (int): First integer number
        b (int): Second integer number

    Raises:
        TypeError: if a or b is not an integer or float

    Returns: integer result of a + b
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
