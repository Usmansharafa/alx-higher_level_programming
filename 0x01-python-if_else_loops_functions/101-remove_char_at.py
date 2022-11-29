#!/usr/bin/python3
def remove_char_at(str, n):
    str_len = len(str)
    if n >= str_len or n < 0:
        return str
    elif n == 0 and str_len > 1:
        return str[1:]
    elif n + 1 < str_len - 1:
        return str[:n] + str[n+1:]
