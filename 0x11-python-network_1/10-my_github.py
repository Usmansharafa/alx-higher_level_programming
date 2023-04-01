#!/usr/bin/python3
"""This module defines a script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"

    resp = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

    if resp.status_code == 200:
        result = resp.json()
        print(result["id"])
    else:
        print("None")
