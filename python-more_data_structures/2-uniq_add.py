#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_it = 0
    temp_list =[]
    for i in my_list:
        if i not in temp_list:
            temp_list.append(i)
    for temp in temp_list:
        add_it += temp
    return add_it
