#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) != 'NoneType':
        for each_key in sorted(a_dictionary.keys()):
            print("{}: {}".format(each_key, a_dictionary[each_key]))
