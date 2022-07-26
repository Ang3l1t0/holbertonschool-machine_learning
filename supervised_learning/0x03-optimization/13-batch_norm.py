#!/usr/bin/env python3
"""Batch Normalization"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """
    batch_norm: normalizes an unactivated output of a neural
                network using batch normalization:
    Args:
        Z: is a numpy.ndarray of shape (m, n) that should be normalized
            m is the number of data points
            n is the number of features in Z
        gamma: is a numpy.ndarray of shape (1, n) containing
                the scales used for batch normalization
        beta: is a numpy.ndarray of shape (1, n) containing
                the offsets used for batch normalization
        epsilon: is a small number used to avoid division by zero

    Returns:
        the normalized Z matrix
    """
    m, stddev = normalization_constants(Z)
    s = stddev ** 2
    Z_norm = (Z - m) / np.sqrt(s + epsilon)
    Z_b_norm = gamma * Z_norm + beta
    return Z_b_norm


def normalization_constants(X):
    """function that calculates the normalization constants of a matrix"""
    m = X.shape[0]
    mean = np.sum(X, axis=0) / m
    stddev = np.sqrt(np.sum((X - mean) ** 2, axis=0) / m)
    return mean, stddev
