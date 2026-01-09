#!/usr/bin/env python3
"""Selects the High, Low, Close, and Volume_BTC columns and every 60th row from the DataFrame. """


def slice(df):
    """Selects the High, Low, Close, and Volume_BTC columns and every 60th row from the DataFrame."""
    return df.loc[:, ['High', 'Low', 'Close', 'Volume_BTC']].iloc[::60]
