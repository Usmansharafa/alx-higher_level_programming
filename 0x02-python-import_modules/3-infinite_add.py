#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    sum = 0
    if len(argv) == 1:
        print(sum)
        exit(0)
    arg_len = len(argv)
    i = 1
    while i < arg_len:
        sum += int(argv[i])
        i += 1

    print(sum)
