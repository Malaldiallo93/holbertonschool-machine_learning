#!/usr/bin/env python3
"""poisson_function"""


class Poisson:
    """
    Class representing a Poisson distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Constructor of the Poisson class.

        Args:
            data (list, optional): List of data to use to
            estimate the distribution.
            lambtha (float, optional): Expected number of occurrences
            in a given time interval.

        Raises:
            ValueError: If lambtha is not a positive value.
            TypeError: If data is not a list.
            ValueError: If data does not contain at least two values.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = float(sum(data) / len(data))
