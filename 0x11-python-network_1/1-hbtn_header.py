#!/usr/bin/python3
"""This module sends a request to url and displays the value of the
X-Request-Id variable found in the header response"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        for item in response.headers.items():
            if item[0] == "X-Request-Id":
                print(item[1])
                break
