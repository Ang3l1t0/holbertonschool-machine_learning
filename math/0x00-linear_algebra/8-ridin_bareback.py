#!/usr/bin/env python3
"""matrix multiplication"""


def mat_mul(mat1, mat2):
    """mat_mul: performs matrix multiplication

    Args:
        mat1: First matrix to multiplicate
        mat2: First matrix to multiplicate
    """
    result = []
    if len(mat1[0]) == len(mat2):
        for i in range(0, len(mat1)):
            temp = []
            for j in range(0, len(mat2[0])):
                s = 0
                for k in range(0, len(mat1[0])):
                    s += mat1[i][k]*mat2[k][j]
                temp.append(s)
            result.append(temp)
        return result
    else:
        return None
