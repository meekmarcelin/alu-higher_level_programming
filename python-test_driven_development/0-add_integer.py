#!/usr/bin/python3
"""addition function module"""


def add_integer(a, b=98):
    """add two number together"""
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

