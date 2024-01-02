#!/usr/bin/python3

'''
    module for simple adding calculations.
'''


def add_integer(a, b=98):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise ValueError("a must be an integer or b must be an integer")

    return int(a) + int(b)
