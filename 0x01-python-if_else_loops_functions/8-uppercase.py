#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            c = ord(c) - ord('a') + ord('A')
            print("{}" .format(chr(c)), end=" ")
        print()
