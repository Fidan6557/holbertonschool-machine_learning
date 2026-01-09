#!/usr/bin/env python3
"""Converting DataFrame to numpy array"""


def array(df):
    """
    Docstring for array

    :param df: Description
    """
    df = df.tail(10).to_numpy()
    return df
