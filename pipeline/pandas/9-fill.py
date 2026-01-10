#!/usr/bin/env python3
"""Filling missing values"""


def fill(df):
    """Filling missing values"""
    df.drop(columns=['Weighted_Price'], inplace=True)
    df['Close'] = df['Close'].fillna(method='ffill')
    df['Volume_(BTC)', 'Volume_(Currency)'] =  df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
    df['High', 'Low', 'Open'] = df['High', 'Low', 'Open'].fillna(df['Close'])
    return df
