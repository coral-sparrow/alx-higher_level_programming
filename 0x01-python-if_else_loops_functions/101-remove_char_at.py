#!/usr/bin/python3

def remove_char_at(str, n):
    t = [s for s in str]
    t.pop(n)
    return ''.join(t)
