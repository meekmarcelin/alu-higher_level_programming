#!/usr/bin/python3
""" print only squares """


def print_square(size):
    """ print squares """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    else:
        s = 0
        while s < size:
            print('#' * size)
            s += 1
