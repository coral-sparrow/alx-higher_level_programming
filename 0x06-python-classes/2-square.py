#!/usr/bin/python3
"""Define a class Square."""


class Square:
    '''
    this is empty class
    '''
    def __init__(self, size=0) -> None:
        '''
        this is consturctor
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
