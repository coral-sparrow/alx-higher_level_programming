#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Define a class functions."""
    try:
        return fct(*args)
    except:
        print(f"Exception: {sys.exc_info()[1]}", file=sys.stderr)
        return None
