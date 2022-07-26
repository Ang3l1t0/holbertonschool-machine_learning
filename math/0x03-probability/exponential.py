#!/usr/bin/env python3
"""Exponential"""


class Exponential():
    """Exponential class
    """
    def __init__(self, data=None, lambtha=1.):
        """Constructor

        Args:
            data:  data to be used to estimate the distribution.
                    Defaults to None.
            lambtha: number of occurences in a given time frame.
                    Defaults to 1.
        """
        self.lambtha = float(lambtha)
        self.e = 2.7182818285
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / float(sum(data) / len(data))

    def pdf(self, x):
        """pmf: Calculates the value of the PMF for a
                given number of “successes”

        Args:
            x: number of “successes”
        """
        if x < 0:
            return 0
        return self.lambtha * self.e**(-self.lambtha*x)

    def cdf(self, x):
        """cdf: CDF for a given number of “successes”

        Args:
            x : number of “successes”
        """
        if x < 0:
            return 0
        return 1 - self.e**(-self.lambtha*x)
