#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = set_1 - set_2
    tmp = set_2 - set_1
    return list(result) + list(tmp)
