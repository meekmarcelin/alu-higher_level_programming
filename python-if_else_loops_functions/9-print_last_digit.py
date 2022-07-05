#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    print("{:d}".format(number % 10), end="")
    return number % 10
