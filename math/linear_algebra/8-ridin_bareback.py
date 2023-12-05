#!/usr/bin/env python3
"""mat_mul function"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
    - mat1 (list of lists): The first input matrix.
    - mat2 (list of lists): The second input matrix.

    Returns:
    - list of lists: The new matrix resulting from matrix multiplication.
      If the two matrices cannot be multiplied, returns None.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*mat2)] for row1 in mat1]
    return result
