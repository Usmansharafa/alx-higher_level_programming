#!/usr/bin/python3
"""This module sends a request to a url and displays the body of
the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
