#!/usr/bin/python3
"""
DOCUMENTATION MUDULE
"""



class Square:
    """
    DIFINE THE SQUARE SIZE
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            riase TypeError("size is integer")
        elif size < 0:
            riase ValueError("size >=0")
        else:
            self._Square__size = size
