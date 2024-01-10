#!/usr/bin/python3
"""Defines a read file function ."""


def write_file(filename="", text=""):
    '''function to open file and read its content to stdout'''
    with open(filename, 'w') as f:
        f.write(text)
