#!/usr/bin/python3
"""Module that defines a function that prints a text with 2 new lines after some specific characters"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after '.', '?', ':' characters.
    
    Args:
        text (str): string to print.

    Raises:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    text_len = len(text)
    while i < text_len and text[i] == " ":
        i += 1
    while i < text_len:
        print(text[i], end='')
        if text[i] in "?:." or text[i] == "\n":
            if text[i] in "?:.":
                print("\n")
            i += 1
            while i < text_len and text[i] == " ":
                i += 1
            continue
        i += 1
