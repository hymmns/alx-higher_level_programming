#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_list = set()

    for each_integer in my_list:
        unique_list.add(each_integer)

    result = sum(unique_list)

    return result
