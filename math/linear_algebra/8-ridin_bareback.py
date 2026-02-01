#!/usr/bin/env python3
"""A function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """A function that performs matrix multiplication"""
    if len(mat1) != len(mat2[0]):
        return None
    else:
        [sum(a * b) for a, b in zip(col,row) for col in zip(*mat2)] for row in mat1]
