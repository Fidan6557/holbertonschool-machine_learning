#!/usr/bin/env python3
""" 13-analyze.py """

def analyze(df):
    """ input -> df
    output -> df with descriptive statistics
    """
    return df.drop(columns=['Timestamp']).describe()
