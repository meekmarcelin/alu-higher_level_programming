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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ list all dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
