#!/usr/bin/env python3
"""Poisson"""


def factorial(n):
    """ returns the factorial of n """
    if n < 0:
        return None
    if n == 0:
        return 1
    if n < 2:
        return 1
    return n * factorial(n-1)


class Poisson():
    """Poisson class
    """
    def __init__(self, data=None, lambtha=1.):
        """Constructor

        Args:
            data: List of the data to be used to estimate the distribution.
                    Defaults to None.
            lambtha: List of the data to be used to estimate the distribution.
                    Defaults to 1.
        """
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) <= 1:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """pmf: Calculates the value of the PMF for a
                given number of “successes”

        Args:
            k: number of “successes”
        """
        if k < 0:
            return 0
        k = int(k)
        return (pow(self.lambtha, k) *
                pow(2.7182818285, -1 * self.lambtha) /
                factorial(k))

    def cdf(self, k):
        """cdf: CDF for a given number of “successes”

        Args:
            k : number of “successes”
        """
        if k < 0:
            return 0
        k = int(k)
        return sum([self.pmf(n) for n in range(k + 1)])
