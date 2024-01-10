#!/usr/bin/python3
"""Defines a file-writing function."""


def from_json_string(my_str):
    '''function to open file and read its content to stdout'''
    import json
    return json.loads(my_str)
