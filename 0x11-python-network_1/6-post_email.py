#!/usr/bin/python3
"""This module sends a POST request to the passed URL and displays the body of
the response"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = ({"email": sys.argv[2]})
    req = requests.post(url, data=email)
    print(req.text)
