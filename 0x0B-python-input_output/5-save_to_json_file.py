#!/usr/bin/python3
"""Defines a file-writing function."""


def save_to_json_file(my_obj, filename):
    '''function to open file and read its content to stdout'''
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
