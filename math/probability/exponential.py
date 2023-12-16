#!/usr/bin/env python3
"""exponential_function"""


class Exponential:
    """
    Represents an exponential distribution.

    Attributes:
        lambtha (float): The expected number of occurrences
        in a given time frame.

    Raises:
        TypeError: If `data` is not a list.
        ValueError: If `data` does not contain at least two values,
        or if `lambtha` is not a positive value.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes an exponential distribution.

        Args:
            data (list, optional): A list of data points to be used
            to estimate the distribution.
            lambtha (float, optional): The expected number of
            occurrences in a given time frame.

        Raises:
            TypeError: If `data` is not a list.
            ValueError: If `data` does not contain at least two values,
            or if `lambtha` is not a positive value.
        """

        # Check if data is None or a list
        if data is not None and not isinstance(data, list):
            raise TypeError('data must be a list')

        # Check if data contains at least 2 values
        if data is not None and len(data) < 2:
            raise ValueError('data must contain multiple values')

        # Check if lambtha is a positive value
        if lambtha <= 0:
            raise ValueError('lambtha must be a positive value')

        # Set lambtha based on data or parameter
        if data is None:
            self.lambtha = lambtha
        else:
            # Calculate lambtha as the inverse of the mean
            self.lambtha = 1 / (sum(data) / len(data))
