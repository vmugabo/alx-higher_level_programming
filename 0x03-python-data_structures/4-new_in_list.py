#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if type(my_list) == list:
        new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list[idx] = new_element
        return new_list
