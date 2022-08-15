#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square instances"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiate a square"""
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """return square dictionary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
