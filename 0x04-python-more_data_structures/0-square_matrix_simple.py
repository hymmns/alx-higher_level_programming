#!/usr/bin/python3


import copy


def square_matrix_simple(matrix=[]):
    result = copy.deepcopy(matrix)
    for each_rows in range(len(result)):
        for column in range(len(result[each_rows])):
            result[each_rows][column] = matrix[each_rows][column] ** 2
    return result
