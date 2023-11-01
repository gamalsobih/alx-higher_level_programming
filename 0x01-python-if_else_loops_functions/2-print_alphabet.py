#!/usr/bin/python3
# 2-print_alphabet.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for c in range(ord('a'), ord('z') + 1):
    print("{:c}".format(c), end="")
