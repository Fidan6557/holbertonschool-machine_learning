#!/usr/bin/env python3
"""Renames the Timestamp column to Datetime, converts it to datetime
format, and returns a DataFrame with only the Datetime and Close columns.
"""
import pandas as pd


def rename(df):
    """Renames the Timestamp column to Datetime, converts it to datetime
    format, and returns a DataFrame with only the Datetime and Close columns.
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], units='ns')
    return df[['Datetime', 'Close']]
