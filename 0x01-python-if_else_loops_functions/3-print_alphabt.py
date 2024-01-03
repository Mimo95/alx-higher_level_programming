#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter in [ord('e'), ord('q')]:
        continue
    print(chr(letter), end="")
