#!/usr/bin/env python3
"""poisson_function"""


class Poisson:
    """
    Represents a Poisson distribution.

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
        Initializes a Poisson distribution.

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
            self.lambtha = float(lambtha)
        else:
            # Calculate lambtha of data
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes."

        Args:
            k (int): The number of "successes."

        Returns:
            float: The PMF value for k.
        """
        # Convert k to an integer
        k = int(k)

        # Check if k is a non-negative integer
        if k < 0 or k != int(k):
            return 0

        # Calculate the PMF value
        pmf_value = (
            (self.lambtha ** k) *
            (2.71828 ** (-self.lambtha)) /
            self.factorial(k)
        )
        return pmf_value

    @staticmethod
    def factorial(self, n):
        """
        Calculates the factorial of a number.

        Args:
            n (int): The number.

        Returns:
            int: The factorial of n.
        """
        if n == 0:
            return 1

        result = 1
        for i in range(1, n + 1):
            result *= i

        return result
