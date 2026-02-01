#!/usr/bin/env python3
"""A function that concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """A function that concatenates two arrays"""
    for i in arr2:
        arr1.append(i)
    return arr1
