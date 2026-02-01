#!/usr/bin/env python3
"""Adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    if mat1.shape != mat2.shape:
        None
    return mat1 + mat2
