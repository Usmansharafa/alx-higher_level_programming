#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            print(f"{chr(ord(char) - 32)}", end='')
            continue
        print(char, end='')
    print()
