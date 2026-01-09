#!/usr/bin/env python3
"""Removing entries where Close has NaN values"""


def prune(df):
    """Removing entries where Close has NaN values"""
    return df.dropna(subset=['Close'])
