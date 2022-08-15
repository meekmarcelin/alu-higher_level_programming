#!/usr/bin/python3
""" create a class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class for square """

    def __init__(self, size, x=0, y=0, id=None):
        """ function for square """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """ square dictinary must be returned """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
