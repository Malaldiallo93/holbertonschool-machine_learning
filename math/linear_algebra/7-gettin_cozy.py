#!/usr/bin/env python3
"""cat_matrices2D function"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
    - mat1 (list of lists): The first input matrix.
    - mat2 (list of lists): The second input matrix.
    - axis (int, optional): The axis along which to concatenate the matrices.

    Returns:
    - list of lists: The new matrix resulting from the concatenation.
      If the two matrices cannot be concatenated, returns None.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
