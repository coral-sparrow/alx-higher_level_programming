#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        return my_list.sorted()[-1]
    else:
        return None
