#!/usr/bin/python3

import argparse


def main():

    parser = argparse.ArgumentParser(
        prog="Infint Add",
        description="Sum all passed arguments",
        epilog="Created By. Mahmoud Gomaa",
        add_help=True,
        exit_on_error=True
    )

    parser.add_argument(
        "numbers",
        nargs='*',
        metavar='N',
        type=int,
        default=[0]
    )

    parser.add_argument(
        '--sum',
        dest='accumelate',
        action='store_const',
        const=sum,
        default=sum,
    )

    args = parser.parse_args()

    print(args.accumelate(args.numbers))


if __name__ == '__main__':
    main()
