#!/usr/bin/python3
"""Defines a file-writing function."""


def to_json_string(my_obj):
    '''function to open file and read its content to stdout'''
    import json
    return json.dumps(my_obj)
