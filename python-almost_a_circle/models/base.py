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
        """return json representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        dict_list = None
        if list_objs is not None:
            dict_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dict_list))
