#!/usr/bin/python3
"""Defines a file-writing function."""


def load_from_json_file(filename):
    '''function to open file and read its content to stdout'''
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
