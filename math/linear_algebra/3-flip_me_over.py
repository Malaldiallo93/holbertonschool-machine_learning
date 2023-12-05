#!/usr/bin/env python3
""" matrix_shape function """


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
    - matrix (list of lists): The input 2D matrix.

    Returns:
    - list of lists: The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]
