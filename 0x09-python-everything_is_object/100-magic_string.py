#!/usr/bin/python3
def magic_string():
    magic_string = getattr(magic_string, 'counter', 0) += 1
    return ', '.join(['BestSchool'] * (magic_string.counter - 1))
