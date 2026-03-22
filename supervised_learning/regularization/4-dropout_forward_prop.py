#!/usr/bin/env python3
"""A function that conducts forward propagation using Dropout:"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """Conducts forward propagation using Dropout"""
    cache = {}
    cache["A0"] = X

    for i in range(L):
        W = weights["W" + str(i + 1)]
        b = weights["b" + str(i + 1)]
        A_prev = cache["A" + str(i)]
        Z = np.matmul(W, A_prev) + b
        A = np.tanh(Z)
        cache["A" + str(i + 1)] = A

        if i != L - 1:
            D = np.random.rand(A.shape[0], A.shape[1]) < keep_prob
            A *= D
            A /= keep_prob
            cache["D" + str(i + 1)] = D

    return cache
