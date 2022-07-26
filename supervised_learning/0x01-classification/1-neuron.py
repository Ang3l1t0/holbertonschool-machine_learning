#!/usr/bin/env python3
"""Classification"""
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
        """W: The weights vector for the neuron.

        Returns:
            W: int
        """
        return self.__W

    @property
    def b(self):
        """b: The bias for the neuron. Upon instantiation

        Returns:
            b: int
        """
        return self.__b

    @property
    def A(self):
        """A: The activated output of the neuron (prediction).

        Returns:
            A: int
        """
        return self.__A
