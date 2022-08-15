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
