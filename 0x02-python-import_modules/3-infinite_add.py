#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    total_sum = 0
    if len(argv) == 1:
        print(total_sum)
        exit(0)
    total_sum = sum([int(num) for num in argv[1:]])
    print(total_sum)
