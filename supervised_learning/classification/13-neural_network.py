#!/usr/bin/env python3
"""class NeuralNetwork"""
import numpy as np


class NeuralNetwork:
    """
    NeuralNetwork class
    """

    def __init__(self, nx, nodes):
        """
        Initializes the NeuralNetwork instance

        Parameters:
        - nx (int): Number of input features
        - nodes (int): Number of nodes in the hidden layer
        """

        # Initialize weights and biases for the hidden layer
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))

        # Initialize weights and biases for the output layer
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0

    def forward_prop(self, X):
        """
        Performs forward propagation for the neural network

        Parameters:
        - X (numpy.ndarray): Input data with shape (nx, m)

        Returns:
        - A1 (numpy.ndarray): Output of the hidden layer
        - A2 (numpy.ndarray): Predicted output
        """

        # Calculate hidden layer output
        Z1 = np.dot(self.__W1, X) + self.__b1
        A1 = 1 / (1 + np.exp(-Z1))

        # Calculate output layer output
        Z2 = np.dot(self.__W2, A1) + self.__b2
        A2 = 1 / (1 + np.exp(-Z2))

        return A1, A2

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neural network

        Parameters:
        - X (numpy.ndarray): Input data with shape (nx, m)
        - Y (numpy.ndarray): Correct labels for the input
        data with shape (1, m)
        - A1 (numpy.ndarray): Output of the hidden layer
        - A2 (numpy.ndarray): Predicted output
        - alpha (float): Learning rate (default is 0.05)
        """

        m = X.shape[1]

        # Compute gradients for the output layer
        dz2 = A2 - Y
        dw2 = np.dot(dz2, A1.T) / m
        db2 = np.sum(dz2, axis=1, keepdims=True) / m

        # Update weights and biases for the output layer
        self.__W2 -= alpha * dw2
        self.__b2 -= alpha * db2

        # Compute gradients for the hidden layer
        dz1 = np.dot(self.__W2.T, dz2) * (A1 * (1 - A1))
        dw1 = np.dot(dz1, X.T) / m
        db1 = np.sum(dz1, axis=1, keepdims=True) / m

        # Update weights and biases for the hidden layer
        self.__W1 -= alpha * dw1
        self.__b1 -= alpha * db1
