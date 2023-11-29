#!/usr/bin/python3

def remove_char_at(str, n):
    t = [s for s in str]
    if n >= 0 and n < len(str):
        t.pop(n)
    return ''.join(t)
