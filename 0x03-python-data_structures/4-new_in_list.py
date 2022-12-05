#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if type(my_list) == list:
        cp_list = my_list.copy()
    if idx < 0 or idx > len(cp_list)-1:
        return cp_list
    else:
        cp_list[idx] = element
        return cp_list
