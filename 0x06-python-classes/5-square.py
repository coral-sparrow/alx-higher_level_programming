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
        self.size = size

    @property
    def size(self):
        '''
        this is consturctor
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        this is consturctor
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        this return area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        this return area of the square
        '''
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
