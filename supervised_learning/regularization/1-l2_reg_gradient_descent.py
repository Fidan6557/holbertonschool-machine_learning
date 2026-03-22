#!/usr/bin/env python3
"""Updates the weights and biases of a neural network using gradient descent with L2 regularization"""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """Updates the weights and biases of a neural network using gradient descent with L2 regularization"""
    m = Y.shape[1]
    dZ = cache['A' + str(L)] - Y
 
    for layer in range(L, 0, -1):
        A_prev = cache['A' + str(layer - 1)]
        W = weights['W' + str(layer)]
        b = weights['b' + str(layer)]
 
        # Compute gradients with L2 regularization term for W
        dW = (1 / m) * np.matmul(dZ, A_prev.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)
 
        # Compute dZ for the previous layer (tanh activation)
        if layer > 1:
            # Derivative of tanh: 1 - A^2
            dA_prev = np.matmul(W.T, dZ)
            dZ = dA_prev * (1 - A_prev ** 2)
 
        # Update weights and biases in place
        weights['W' + str(layer)] = W - alpha * dW
        weights['b' + str(layer)] = b - alpha * db
