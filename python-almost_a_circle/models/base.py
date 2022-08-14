#!/usr/bin/python3
""" Create a class """
import json


class Base:
    """ create a real base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ first base function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
