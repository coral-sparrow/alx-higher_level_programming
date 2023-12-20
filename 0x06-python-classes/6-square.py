#!/usr/bin/python3
"""Define a class Square."""


class Square:
    '''
    this is empty class
    '''
    def __init__(self, size=0, position=(0, 0)) -> None:
        '''
        this is consturctor
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if all([x < 0 for x in value]):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
                if self.position[1] > 0:
                    print('#' * self.size)
                else:
                    print(' ' * self.position[0] + '#' * self.size)
