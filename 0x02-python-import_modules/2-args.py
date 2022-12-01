#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{arg_len - 1} arguments:")
        for i in range(1, arg_len):
            print(f"{i}: {sys.argv[i]}")
