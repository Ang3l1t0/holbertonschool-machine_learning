#!/usr/bin/env python3

""" Calculate the shape of a matrix, returned as a list of integers """


def matrix_shape(matrix):
    """matrix_shape :  that calculates the shape of a matrix

    Args:
        matrix: matrix to be dimensioned
    """
    if not matrix:
        return None

    if not isinstance(matrix[0], list):
        return [len(matrix)]

    return [len(matrix)] + matrix_shape(matrix[0])
