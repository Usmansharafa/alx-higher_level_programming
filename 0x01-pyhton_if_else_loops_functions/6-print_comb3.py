#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while j < 10:
        print(f"{i}{j}", end='')
        if i == 8 and j == 9:
            print()
            break
        print(", ", end='')
        j += 1
