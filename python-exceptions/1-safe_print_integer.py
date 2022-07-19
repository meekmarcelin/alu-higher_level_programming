#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        retutn(true)
    except (ValueError, TypeError):
        return(False)
