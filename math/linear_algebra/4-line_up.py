#!/usr/bin/env python3
"""Adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise """
    return [a+b for a,b in zip(arr1, arr2)]
