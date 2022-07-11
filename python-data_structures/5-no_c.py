#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    letter_count = 0
    for letter in my_string_list:
        if letter == 'c' or letter == 'c':
            my_string_list[letter_count] = ""
        letter_count += 1
    return "".join(my_string_list)
