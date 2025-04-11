#!/usr/bin/env python3
"""
Creates a pandas DataFrame from a NumPy
ndarray with alphabetical column labels.
"""

import pandas as pd
import numpy as np


def from_numpy(array):
    """
    Converts a NumPy array into a pandas DataFrame.

    Parameters:
        array (np.ndarray): The NumPy array to convert. 
        Assumes the array has two dimensions (rows and columns).

    Returns:
        pd.DataFrame: A DataFrame created from the NumPy array with 
        alphabetically labeled columns (A, B, C, ..., up to Z). 
        Supports up to 26 columns.
    """
    # Get the number of columns from the array
    _, num_cols = array.shape

    # Alphabet for generating column labels
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
    # Generate column labels (A, B, C, ...) up to a maximum of 26 columns
    column_labels = list(alphabet[:min(num_cols, 26)])

    # Create the DataFrame with the generated column labels
    df = pd.DataFrame(array, columns=column_labels)

    return df
