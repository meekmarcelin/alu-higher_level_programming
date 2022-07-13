#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    greater = 0
    for key, value in a_dictionary.items():
        if value > greater:
            greater = value
    for key, value in a_dictionary.items():
        if value == greater:
            return key
