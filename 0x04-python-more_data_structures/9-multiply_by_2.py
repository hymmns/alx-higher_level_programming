#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    result = {}

    for each_key, value in a_dictionary.items():
        result[each_key] = value * 2

    return result
