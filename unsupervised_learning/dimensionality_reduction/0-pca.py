#!/usr/bin/env python3
"""Principal Component Analysis (PCA)"""
import numpy as np


def pca(X, var=0.95):
    """PCA"""
    U, S, Vt = np.linalg.svd(X, full_matrices=False)

    squared_singular_values = S**2
    total_variance = np.sum(squared_singular_values)
    cumulative_variance_ratio = np.cumsum(squared_singular_values) / total_variance
    nd = np.argmax(cumulative_variance_ratio >= var) + 1
    W = Vt[:nd].T
    return W
