#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if type(my_list) == list:
        cp_list = my_list.copy()
    if idx < 0 or idx > len(cp_list):
        return cp_list
    else:
        cp_list[idx] = new_element
        return cp_list
