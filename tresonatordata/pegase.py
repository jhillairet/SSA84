# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:51:30 2022

@author: JH218595
"""
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
plt.rcParams['toolbar'] = 'toolmanager'

def load_pegase_data(filename: str) -> pd.DataFrame:
    """
    Load Pegase data file (continuous data acquisition)

    Parameters
    ----------
    filenamme : str
        filename path

    Returns
    -------
    df : pandas DataFrame
    """
    df = pd.read_csv(filename, delimiter='\t')
    # forge date timestamp 
    df['date'] = pd.to_datetime(df['Unnamed: 0']+' '+df['Unnamed: 1'], dayfirst=True)
    df = df.set_index('date')
    # clean up
    df = df.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1)
    
    return df

def load_multiple_pegase_data(filenames: list) -> pd.DataFrame:
    """
    Load and concatenate multiple Pegase datafile into a single DataFrame.

    Parameters
    ----------
    filenames : list of string
        List of filenames

    Returns
    -------
    df : pandas DataFrame
    """
    return pd.concat([load_pegase_data(filename) for filename in filenames])
