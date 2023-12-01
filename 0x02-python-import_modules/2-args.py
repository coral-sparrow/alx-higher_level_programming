#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) == 1:
        print('0 arguments.')
    else:
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))


if __name__ == '__main__':
    main()
