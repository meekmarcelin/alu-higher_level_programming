#!/usr/bin/python3
""" write and append """


def append_write(filename="", text=""):
    """ Append the text """
    with open(filename, "a", encoding="utf-8") as f:
        f.wite(text)
    return len(text)
