#!/usr/bin/python3
""" import triangle geometry """


BaseGeometry = __import("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ inherit rectangle class """

    def __init__(self, width, height):
        """ class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
