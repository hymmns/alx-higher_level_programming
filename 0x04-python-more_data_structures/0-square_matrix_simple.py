#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = [[0 for each_column in each_row] for each_row in matrix]
    for each_rows in range(len(result)):
        for column in range(len(result[each_rows])):
            result[each_rows][column] = matrix[each_rows][column] ** 2
    return result
