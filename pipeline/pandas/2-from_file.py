#!/usr/bin/env python3
"""
A functionthat loads data from a file as a pd.DataFrame

"""
import pandas as pd


def from_file(filename, delimiter): 
    """ creates a pd.DataFrame from a file """
    return pd.read_csv(filename, delimiter=delimiter)
