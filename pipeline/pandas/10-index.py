#!/usr/bin/env python3
"""My module document"""


def index(df):
    """Indexing the DataFrame"""
    df = df.set_index('Timestamp')
    return df
