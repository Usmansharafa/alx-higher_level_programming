#!/usr/bin/python3
"""This module contains a script that sends a request to a url and displays
the value of X-Request-Id in the header"""


if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])

    print(req.headers['X-Request-Id'])
