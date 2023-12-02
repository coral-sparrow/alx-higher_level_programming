#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) > 1:
        n = [int(x) for x in sys.argv[1:]]
    else:
        n = [0]

    print(sum(n))


if __name__ == '__main__':
    main()
