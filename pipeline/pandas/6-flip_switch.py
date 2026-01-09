#!/usr/bin/env python3
"""Sorts a DataFrame in reverse chronological order and transposes it."""


def flip_switch(df):
    """Sorts a DataFrame in reverse chronological order and transposes it."""
    return df[::-1].T
