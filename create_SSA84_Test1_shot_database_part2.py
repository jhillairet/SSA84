# -*- coding: utf-8 -*-
"""
Create a resumed database of the SSA84 TaskB RF tests.
"""
from glob import glob
from tresonatordata.tresonatordata import TResonatorData
from tqdm import tqdm
from os.path import dirname, abspath, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
directories = [
    # 'data/2022-02-02_SSA84_RF_tests', # Part 1
    # 'data/2022-02-03_SSA84_RF_tests',
    # 'data/2022-02-04_SSA84_RF_tests',
    # 'data/2022-02-14_SSA84_RF_tests',
    # 'data/2022-02-15_SSA84_RF_tests',
    # 'data/2022-02-16_SSA84_RF_tests',
    # 'data/2022-02-17_SSA84_RF_tests',
    'data/2022-03-11_SSA84_RF_tests', # Part 2   
    'data/2022-03-14_SSA84_RF_tests',  
    ]

# get all .hdf files in all directories
hdf_files = []
for directory in directories:
    name_filter = join(dirname(abspath(__file__)), directory, '*.hdf')
    hdf_files.extend(glob(name_filter))

#%%
def find_shots_indices(array, threshold):
    """
    Returns the start and stop arrays indices corresponding to RF shot.

    Parameters
    ----------
    array : numpy array
        Array to threshold on
    threshold : float
        threshold to appy

    Returns
    -------
    idx_starts : list of int
    idx_stops : list of int
    """
    # indices of values above threshold
    idx_thres = np.nonzero(array > threshold)[0]
    if idx_thres.size > 0:  # not empty
        # find indices where we change the RF shot   
        idx_starts = np.append(idx_thres[0], idx_thres[1:][np.diff(idx_thres) > 1])
        idx_stops = np.append(idx_thres[0:-1][np.diff(idx_thres) > 1], idx_thres[-1])
 
        return idx_starts, idx_stops
    else:
        return None, None

def split_array(array, idx_starts, idx_stops):
    """
    Split an numerical array into sub-arrays according to start and stop indices.

    Parameters
    ----------
    array : numpy array
    idx_starts : list of int
    idx_stops : list of int

    Returns
    -------
    arrays : list of array
    """
    arrays = []    
    for idx_start, idx_stop in zip(idx_starts, idx_stops):
        arrays.append(array[idx_start:idx_stop])
    return arrays

def stats(subarray_list):
    """
    Extract the (mean, std, min, max) values of each subarrays

    Parameters
    ----------
    subarray_list : list of numpy array

    Returns
    -------
    stats : list of array

    """
    stats = []
    for arr in subarray_list:
        if arr.size > 0: # not empty
            stats.append([np.mean(arr), np.std(arr), np.min(arr), np.max(arr)])

    return stats

#%%
database = pd.DataFrame()

V1_stats = []
V2_stats = []
Pi_stats = []
Pr_stats = []
JR3_stats = []
JR4_stats = []
time_stats = []

for hdf_file in hdf_files:
    data = TResonatorData(hdf_file)

    idx_starts, idx_stops = find_shots_indices(data.df['V1 [V]'].values, 50)

    if idx_starts is not None:
        times = split_array(data.df['time_absolute'].values, idx_starts, idx_stops)
        subV1s = split_array(data.df['V1 [V]'].values, idx_starts, idx_stops)
        subV2s = split_array(data.df['V2 [V]'].values, idx_starts, idx_stops)
        subPis = split_array(data.df['Pi [W]'].values, idx_starts, idx_stops)
        subPrs = split_array(data.df['Pr [W]'].values, idx_starts, idx_stops)
        subJR3s = split_array(data.df['JR3'].values, idx_starts, idx_stops)
        subJR4s = split_array(data.df['JR4'].values, idx_starts, idx_stops)        
        
        time_stats.append([t.flatten()[0] for t in times if t.size > 0])
        V1_stats.append(stats(subV1s))
        V2_stats.append(stats(subV2s))
        Pi_stats.append(stats(subPis))
        Pr_stats.append(stats(subPrs))
        JR3_stats.append(stats(subJR3s))
        JR4_stats.append(stats(subJR4s))

#%%
times_mmm = np.hstack(np.array(time_stats, dtype=object))
V1_mmm = np.vstack(np.array(V1_stats, dtype=object))
V2_mmm = np.vstack(np.array(V2_stats, dtype=object))
Pi_mmm = np.vstack(np.array(Pi_stats, dtype=object))
Pr_mmm = np.vstack(np.array(Pr_stats, dtype=object))
JR3_mmm = np.vstack(np.array(JR3_stats, dtype=object))
JR4_mmm = np.vstack(np.array(JR4_stats, dtype=object))

#%%
fig, ax = plt.subplots()
ax.plot(times_mmm, V1_mmm[:,0], '.', color='C0')
ax.plot(times_mmm, V2_mmm[:,0], '.', color='C1')


#%%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots()
    ax.plot(times_mmm, Pi_mmm[:,0], '.', color='C0')
    ax.plot(times_mmm, Pr_mmm[:,0], '.', color='C1')
    ax.set_xlabel('shot #')
    ax.set_ylabel('voltage [V]')
    fig.autofmt_xdate(rotation=45)
    ax.set_title('SSA84 - Part 2')
    # fig.savefig('SSA84_Part2_voltage_vs_shotnumber.png', dpi=150)

#%%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots()
    ax.plot( V1_mmm[:,0], '.', color='C0')
    ax.plot( V2_mmm[:,0], '.', color='C1')
    ax.set_xlabel('shot #', fontsize=14)
    ax.set_ylabel('voltage [V]', fontsize=14)
    fig.autofmt_xdate(rotation=45)
    ax.set_title('SSA84 - Part 2', fontsize=14)
    fig.tight_layout()
    # fig.savefig('SSA84_Part2_voltage_vs_day.png', dpi=150)


# %%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots()
    ax.plot(np.max([JR3_mmm[:,3], JR4_mmm[:,3]], axis=0), '.', color='C1', label='max pressure during shot', alpha=0.4)
    ax.plot(np.min([JR3_mmm[:,2], JR4_mmm[:,2]], axis=0), '.', color='C0', label='shot start pressure', alpha=0.4)
    ax.set_yscale('log')
    ax.legend()
    ax.set_xlabel('day shot #')
    ax.set_ylabel('pressure [Pa]')
    ax.set_title('SSA84 - Part 2')