#!/usr/bin/python3
""" create a class for python """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ function for square """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """ dic to return square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
