#!/usr/bin/env python3
"""adds two arrays"""


def add_arrays(arr1, arr2):
    """add_arrays : adds two arrays element-wise

    Args:
        arr1: First array to sum
        arr2: Second array to sum
    """
    if len(arr1) == len(arr2):
        result = [arr1[position] + arr2[position]
                  for position in range(len(arr1))]

        return result
    return None
