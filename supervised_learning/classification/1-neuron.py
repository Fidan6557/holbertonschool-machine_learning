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

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0

    @property
    def W(self):
        """weights vector for the neuron"""
        return self.__W
    
    @property
    def b(self):
        """bias for the neuron"""
        return self.__b
    
    @property
    def A(self):   
        """activated output of the neuron (prediction)"""
        return self.__A
