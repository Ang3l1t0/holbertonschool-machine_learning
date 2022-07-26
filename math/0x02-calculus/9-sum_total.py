#!/usr/bin/env python3
"""Summation"""


def summation_i_squared(n):
    """summation_i_squared: calculate the squared

    Args:
        n: stopping condition
    """
    if not isinstance(n, int) or n <= 0:
        return None
    elif n == 1:
        return n
    return sum(map(lambda i: i ** 2, range(1, n + 1)))
