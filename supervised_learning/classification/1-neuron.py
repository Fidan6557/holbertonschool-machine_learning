#!/usr/bin/env python3
"""a class that defines a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """class constructor"""

    def __init__(self, nx):
        """class constructor"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0
