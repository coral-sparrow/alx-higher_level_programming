#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        c = my_list.copy()
        c.sort()
        return c[-1]
    else:
        return None
