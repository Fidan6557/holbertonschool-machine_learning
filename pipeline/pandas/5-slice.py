#!/usr/bin/env python3
"""Slices the DataFrame every 60 rows and selects specific columns."""


def slice(df):
   """Slices the DataFrame every 60 rows and selects specific columns."""
   return df.loc[:, ['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
