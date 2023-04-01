#!/usr/bin/python3
"""This module sends a request to a url and displays the body of
the response"""


if __name__ == "__main__":
    import sys
    import requests

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
