#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Define a class functions."""
    try:
        fct()
    except:
        print(f"Exception: {sys.exc_info}", file=sys.stderr)
        return None
