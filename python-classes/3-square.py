#!/usr/bin/python3
"""
MORE MODULES
"""


class Square:
    """DEFINE A SQUARE""

    def __init__(self, size=0):
        """
        creates an instance of square
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        FInds area of the square
        """
        return self.__size * self.__size



