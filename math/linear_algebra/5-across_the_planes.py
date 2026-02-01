#!/usr/bin/env python3
"""Adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    if len(mat1) != len(mat2):
        None
    return [a+b for a, b in zip(mat1, mat2)]
