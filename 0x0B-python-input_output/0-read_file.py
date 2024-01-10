#!/usr/bin/python3
"""Defines a read file function ."""


def read_file(filename=""):
    '''function to open file and read its content to stdout'''
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line, end='')
