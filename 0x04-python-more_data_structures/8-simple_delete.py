#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key, None) != None:
        return a_dictionary.pop(key)
