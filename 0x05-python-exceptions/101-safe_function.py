#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        result = None
    return result
