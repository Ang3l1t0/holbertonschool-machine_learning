#!/usr/bin/env python3
"""Neuron"""
import numpy as np


class Neuron():
    """Single neuron performing binary classification"""

    def __init__(self, nx):
        """Constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.normal(0, 1, (1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """forward_prop: Calculates the forward propagation of the neuron

        Args:
            X : with shape (nx, m) that contains the input data

        Returns:
            the private attribute __A
        """
        Z = np.matmul(self.W, X) + self.b
        self.__A = self.sigmoid(Z)
        return self.A

    def sigmoid(self, Y):
        """define the sigmoid activation function"""
        return 1 / (1 + np.exp(-1 * Y))

    def cost(self, Y, A):
        """cost: defnine the cost function

        Args:
            Y : with shape (1, m) that contains the correct
                labels for the input data
            A : containing the activated output of the neuron for each example

        Returns:
            the cost
        """
        # classification pb: use the cross-entropy function
        m = Y.shape[1]
        return (-1 / m) * np.sum(
            Y * np.log(A) + (1 - Y) * (np.log(1.0000001 - A)))
