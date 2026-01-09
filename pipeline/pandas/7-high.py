#!/usr/bin/env python3
"""Sorts the DataFrame by the High column in descending order"""


def high(df):
    """Sorts the DataFrame by the High column in descending order"""
    return df.sort_values(by='High', ascending=False)
