#!/usr/bin/env python3
"""np_matmul function"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
    - mat1 (numpy.ndarray): The first input numpy array.
    - mat2 (numpy.ndarray): The second input numpy array.

    Returns:
    - numpy.ndarray: The new matrix resulting from matrix multiplication.
    """
    return np.dot(mat1, mat2)
