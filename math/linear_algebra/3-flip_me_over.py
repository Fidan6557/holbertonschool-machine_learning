#!/usr/bin/env python3
"""The transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """The transpose of a 2D matrix"""
    return [list(row) for row in zip(*matrix)]
