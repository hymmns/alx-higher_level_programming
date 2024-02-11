#!/usr/bin/python3


def best_score(a_dictionary):
    key = None
    score = 0

    if a_dictionary is not None:
        for each_key, each_value in a_dictionary.items():
            if each_value > score:
                score = each_value
                key = each_key

        return key

    else:
        return None
