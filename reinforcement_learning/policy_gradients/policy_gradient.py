#!/usr/bin/env python3
"""
    Policy Gradient
"""

import numpy as np


def softmax(x):
    """Compute softmax values for each set of scores in x."""
    e_x = np.exp(x - np.max(x))  # Stability trick
    return e_x / e_x.sum()


def policy_gradient(state, weight):
    """
    Compute the Monte-Carlo policy gradient based
    on a state and a weight matrix.
    Args:
        state (numpy.ndarray): A 1D array representing
        the current observation of the environment.
        weight (numpy.ndarray): A 2D array of random weights.
    Returns:
        tuple: The action (int) chosen according to the policy
        and the corresponding gradient.
    """
    probs = softmax(np.dot(state, weight))
    action = int(np.random.choice(len(probs), p=probs))

    # Compute the gradient
    d_log = np.zeros_like(probs)
    d_log[action] = 1 / probs[action]
    grad = np.outer(state, d_log - probs)

    return action, grad
