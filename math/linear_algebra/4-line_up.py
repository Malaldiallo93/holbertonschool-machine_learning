#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
    - arr1 (list of ints/floats): The first input array.
    - arr2 (list of ints/floats): The second input array.

    Returns:
    - list of ints/floats: The resulting array after element-wise addition.
      If arr1 and arr2 are not the same shape, returns None.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
