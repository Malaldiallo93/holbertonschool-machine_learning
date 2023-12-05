#!/usr/bin/env python3
def matrix_transpose(matrix):
    """
    Transposes a 2D matrix.

    Args:
    - matrix (list of lists): The input 2D matrix.

    Returns:
    - list of lists: The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]
