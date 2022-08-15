#!/usr/bin/python3
"""create a base class"""

import json
import csv


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json must be returned """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function to save json"""
        dict_list = None
        if list_objs is not None:
            dict_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dict_list))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is not None:
            if cls.__name__ == "Square":
                dict_list = [['id', 'size', 'x', 'y']]
                dict_list.extend([[i.id, i.size, i.x, i.y] for i in list_objs])
            else:
                dict_list = [['id', 'width', 'height', 'x', 'y']]
                c_li = [[i.id, i.width, i.height, i.x, i.y] for i in list_objs]
                dict_list.extend(c_li)
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """ update and add """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return instance """
        if cls.__name__ == 'square':
            shape = cls(1)
        else:
            shape = cls(1, 1)
        shape.update(**dictionary)
        return shape
