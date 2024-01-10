#!/usr/bin/python3
"""Defines a read file function ."""


def append_write(filename="", text=""):
    '''function to open file and read its content to stdout'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
