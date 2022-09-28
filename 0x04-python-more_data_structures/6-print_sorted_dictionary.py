#!/usr/bin/python3
def number_keys(a_dictionary):
    sorted_list = list(a_dictionary)
    sorted_list.sort()

    for i in sorted_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
