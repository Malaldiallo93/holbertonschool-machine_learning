#!/usr/bin/env python3
import numpy as np
"""class NeuralNetwork"""


class NeuralNetwork:
    def __init__(self, nx, nodes):
        """
        Constructor method for NeuralNetwork instances.

        Args:
            nx (int): The number of input features.
            nodes (int): The number of nodes in the hidden layer.

        Raises:
            TypeError: If nx or nodes is not an integer.
            ValueError: If nx or nodes is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        elif nodes < 1:
            raise ValueError('nodes must be a positive integer')

        # Initialize weights and biases
        self.__W1 = np.random.normal(0, 1, (nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0

        self.__W2 = np.random.normal(0, 1, (1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network.

        Args:
            X (numpy.ndarray): Input data with shape (nx, m).

        Returns:
            Tuple: Activated outputs for the hidden layer (__A1)
            and the output layer (__A2).
        """
        Z1 = np.dot(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + np.exp(-Z1))

        Z2 = np.dot(self.W2, self.A1) + self.b2
        self.__A2 = 1 / (1 + np.exp(-Z2))

        return self.A1, self.A2
