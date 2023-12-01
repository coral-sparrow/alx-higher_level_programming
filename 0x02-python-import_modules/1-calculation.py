#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    r1 = add(a, b)
    r2 = sub(a, b)
    r3 = mul(a, b)
    r4 = div(a, b)
    print('{} + {} = {}'.format(a, b, r1))
    print('{} - {} = {}'.format(a, b, r2))
    print('{} * {} = {}'.format(a, b, r3))
    print('{} / {} = {}'.format(a, b, r4))


if __name__ == '__main__':
    main()
