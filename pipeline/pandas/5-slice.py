#!/usr/bin/env python3
"""Slices the DataFrame every 60 rows and selects specific columns."""


def slice(df):
    """Return High, Low, Close, Volume_(BTC) columns every 60 rows."""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
