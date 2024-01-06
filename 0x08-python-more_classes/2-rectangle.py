#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Define a class Rectangle."""
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

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
