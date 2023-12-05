#!/usr/bin/env python3
"""np_cat function"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
    - mat1 (numpy.ndarray): The first input numpy array.
    - mat2 (numpy.ndarray): The second input numpy array.
    - axis (int, optional): The axis along which to concatenate the matrices.

    Returns:
    - numpy.ndarray: The new matrix resulting from the concatenation.
    """
    return np.concatenate((mat1, mat2), axis=axis)
