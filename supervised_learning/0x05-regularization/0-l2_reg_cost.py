#!/usr/bin/env python3
"""Regularization Cost"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """function that calculates the cost of a nn with L2 regularization"""
    # function that calculates the Frobenius norm (when ord=None)
    # numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)
    frobenius_norm = 0
    for key, weight in weights.items():
        if key[0] == 'W':
            frobenius_norm += np.linalg.norm(weight)
    cost += lambtha / (2 * m) * frobenius_norm
    return cost
