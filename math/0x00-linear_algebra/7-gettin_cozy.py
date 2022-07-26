#!/usr/bin/env python3
"""concatenates two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """cat_matrices2D: concatenates two matrices along a specific axis

    Args:
        mat1: First matrix to concatenate
        mat2: Second matrix to concatenate
        axis (optional): Defaults to 0.
    """
    result = []
    # Check axis 1
    if axis == 1 and len(mat1) == len(mat2):
        for count, value in enumerate(mat1):
            result.append(value + mat2[count])
        return result

    # Check axis 0
    elif axis == 0 and len(mat1[0]) == len(mat2[0]):
        for row in mat1:
            result.append(list(row))
        for row in mat2:
            result.append(list(row))

        return result

    return None
