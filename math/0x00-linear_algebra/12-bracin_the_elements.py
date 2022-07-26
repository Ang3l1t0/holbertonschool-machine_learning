#!/usr/bin/env python3
"""Bracing The Elements"""


def np_elementwise(mat1, mat2):
    """np_elementwise: performs element-wise addition,
                        subtraction, multiplication, and division

    Args:
        mat1: First matrix to realize operations
        mat2: Second matrix to realize operations
    """
    sum_ = (mat1 + mat2)[0:]
    subs_ = (mat1 - mat2)[0:]
    mul_ = (mat1 * mat2)[0:]
    div_ = (mat1 / mat2)[0:]

    return sum_, subs_, mul_, div_
