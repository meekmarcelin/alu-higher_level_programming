#!/usr/bin/python3
""" Inherets from python """


def inherits_from(obj, a_class):
    """ return true if class is inhereted else false """
    return (issubclass(type(obj), a_class) and type(obj) != a_class
