#!/usr/bin/python3
"""This module sends a POST request to the passed URL and displays the body of
the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = urllib.parse.urlencode({"email": sys.argv[2]})
    email = email.encode("ascii")
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
