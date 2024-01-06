#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Define a class Rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''return the width private attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width private attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''return the height private attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height private attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''return the rectangle area'''
        return self.height * self.width

    def perimeter(self):
        '''return the recangle perimeter'''
        if self.height == 0 or self.width == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        '''return the recangle representation in # '''

        if self.width == 0 or self.height == 0:
            return ''

        st = ''
        for i in range(self.height):
            if i == self.height - 1:

                st += f'{self.print_symbol}' * self.width
            else:
                st += f'{self.print_symbol}' * self.width + '\n'
        return st

    def __repr__(self) -> str:
        '''return the recangle string representation'''

        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''Recangle destructor '''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compares 2 rectangles areas'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.are() >= rect_2.are():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        ''' alternative contructor to create sqare'''
        return cls(width=size, height=size)
