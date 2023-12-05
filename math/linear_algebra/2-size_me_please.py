#!/usr/bin/env python3
""" matrix_shape function """


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list.

    Args:
        matrix (n-dimensional array): The matrix to find the shape of.

    Returns:
        list: The dimensions of the array as a list.
    """
    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
