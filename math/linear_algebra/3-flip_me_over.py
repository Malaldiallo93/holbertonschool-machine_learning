#!/usr/bin/env python3
""" matrix_transpose function """


def matrix_transpose(matrix):
    """
    Transposes a matrix

    Args:
        matrix (2Dimensional list): The matrix to transpose

    Returns:
        list: A new matrix corresponding to the transpose of `matrix`
    """
    return [list(row) for row in zip(*matrix)]
