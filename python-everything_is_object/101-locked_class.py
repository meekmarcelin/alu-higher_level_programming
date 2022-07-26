#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass
    """No class or object attribut, Except for first_time
    """
    def __setattr__(self, attribut, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedCladd' object has no attribut'" + attribute + "'")
