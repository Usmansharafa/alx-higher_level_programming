#!/usr/bin/python3
"""This module contains a script that fetches a url"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
