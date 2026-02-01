#!/usr/bin/env python3
"""A function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """A function that concatenates two matrices along a specific axis"""
    if not mat1 or not mat2:
        return None
    
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        if len(mat1) != len(nat2):
            return None 
        return [r1 + r2 for r1, r2 in zip(mat1, mat2)]

    return None
