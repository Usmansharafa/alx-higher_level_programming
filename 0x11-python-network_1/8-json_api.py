#!/usr/bin/python3
"""This module send a POST request to a url with a letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) != 2 else sys.argv[1]
    param = {"q": letter}
    req = requests.post(url, data=param)
    try:
        req = req.json()
        if len(req) == 0:
            print("No result")
        else:
            print(f"[{req['id']}] {req['name']}")
    except ValueError:
        print("Not a valid JSON")
