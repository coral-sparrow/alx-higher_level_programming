#!/usr/bin/python3

from add_0 import add


def main():
    a = 1
    b = 2
    r = add(a, b)

    print('{} + {} = {}'.format(a, b, r))


if __name__ == '__main__':
    main()
