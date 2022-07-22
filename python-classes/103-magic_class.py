#!/usr/bin/python3
""" Do some magic math"""
import math
""" Do some magic math"""


class MagicClass:
    """creates circle instance"""
    def __init__(self, radius=0):
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi * self._MagicClass__radius)
