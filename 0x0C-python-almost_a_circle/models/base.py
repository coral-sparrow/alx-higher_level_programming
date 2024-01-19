#!/usr/bin/python3
''' base class for the project '''


class Base():
    ''' the base class definition '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
