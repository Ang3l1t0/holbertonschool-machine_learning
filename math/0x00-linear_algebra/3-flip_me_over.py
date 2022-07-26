#!/usr/bin/env python3
"""transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """matrix_transpose: returns the transpose of a 2D matrix.

    Args:
        matrix: matrix that is received to be transposed
    """
    result = [[matrix[j][i]
               for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result
