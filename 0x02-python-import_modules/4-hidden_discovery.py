#!/usr/bin/python3

from hidden_4 import *


g = globals().copy()


def main():
    r = []

    for k, v in g.items():
        if not k.startswith('__'):
            r.append(k)
    for i in sorted(r):
        print(i)


if __name__ == '__main__':
    main()
