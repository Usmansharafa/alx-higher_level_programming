#!/usr/bin/python3
"""This module defines a script that lists 10 recent commits of a repository"""


if __name__ == "__main__":
    import requests
    import sys

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    resp = requests.get(url)
    result = resp.json()
    try:
        for i in range(10):
            print(f"{result[i]['sha']}: \
{result[i]['commit']['author']['name']}")
    except IndexError:
        pass
