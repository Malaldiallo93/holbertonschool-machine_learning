#!/usr/bin/env python3
"""np_elementwise function"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
    - mat1 (numpy.ndarray): The first input numpy array.
    - mat2 (numpy.ndarray): The second input numpy array.

    Returns:
    - tuple of numpy.ndarrays: The element-wise sum, difference.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
