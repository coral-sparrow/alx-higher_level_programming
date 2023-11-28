#!/usr/bin/python3

def uppercase(str):
    my_str = ''
    for i in str:
        if ord(i) not in range(97, 123):
            my_str += i
        else:
            my_str += chr(ord(i) - 32)
    print('{}'.format(my_str))
