#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary
    list_keys = list(new_dic)

    for i in list_keys:
        new_dic[i] *= 2

    return (new_dic)
