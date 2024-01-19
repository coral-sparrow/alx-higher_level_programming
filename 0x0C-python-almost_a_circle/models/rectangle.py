#!/usr/bin/python3
from base import Base
"""Define a class Rectangle."""


class Rectangle(Base):
    '''the Rectangle class the inherits from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' init method of the rectangle class'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter/seter function'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''height getter/setter function'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x getter/setter function'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y getter/setter function'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
