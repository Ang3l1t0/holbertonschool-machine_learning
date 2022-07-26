#!/usr/bin/env python3
"""adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """add_matrices2D: adds two matrices element-wise

    Args:
        mat1: First matrix to sum
        mat2: Second matrix to sum
    """
    if len(mat1[0]) == len(mat2[0]):
        result = [[mat1[x][y] + mat2[x][y]
                   for y in range(len(mat1[0]))] for x in range(len(mat1))]
        return result
    return None
