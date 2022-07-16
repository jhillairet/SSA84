#%%
import pandas as pd
import matplotlib.pyplot as plt
from tresonatordata.pegase import load_multiple_pegase_data
import numpy as np

plt.rcParams['toolbar'] = 'toolmanager'

#%% 22/11/2021 -> 08/01/2022 Conditioning 
files = ['data/TaskB/pegase/continuous_data_2021-11-22_baking1-and-2-leak.txt']

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 300] = np.NaN
df['R_TCF'][df['R_TCF'] > 300] = np.NaN

with plt.style.context('seaborn'):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12.5, 5.5))
    df.plot(y='R_TB70', ax=axes[0], label='Resonator (TC avg)')
    df.rolling(10).mean().plot(y='R_TCF', ax=axes[0], label='TC DUT', color='C3')
    axes[0].set_ylabel('Temperature [°C]')
    
    df.plot(y='R_JR3', ax=axes[1], color='C1')
    df.plot(y='R_JR4', ax=axes[1], color='C4')
    axes[1].set_yscale('log')
    axes[1].set_ylabel('Pressure [Pa]')
    
    fig.tight_layout()

#%% 15/02/2022 -> 17/02/2022 RF Tests
files = ['data/TaskB/pegase/continuous_data_2022-02_16-17.txt']

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 300] = np.NaN
df['R_TCF'][df['R_TCF'] > 300] = np.NaN

with plt.style.context('seaborn'):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12.5, 5.5))
    df.plot(y='R_TB70', ax=axes[0], label='Resonator (TC avg)')
    df.rolling(10).mean().plot(y='R_TCF', ax=axes[0], label='TC DUT', color='C3')
    axes[0].set_ylabel('Temperature [°C]')
    
    df.plot(y='R_JR3', ax=axes[1], color='C1')
    df.plot(y='R_JR4', ax=axes[1], color='C4')
    axes[1].set_yscale('log')
    axes[1].set_ylabel('Pressure [Pa]')
    
    fig.tight_layout()
    
files = ['data/TaskB/pegase/continuous_data_2022-02_.txt']

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 300] = np.NaN
df['R_TCF'][df['R_TCF'] > 300] = np.NaN

with plt.style.context('seaborn'):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12.5, 5.5))
    df.plot(y='R_TB70', ax=axes[0], label='Resonator (TC avg)')
    df.rolling(10).mean().plot(y='R_TCF', ax=axes[0], label='TC DUT', color='C3')
    axes[0].set_ylabel('Temperature [°C]')
    
    df.plot(y='R_JR3', ax=axes[1], color='C1')
    df.plot(y='R_JR4', ax=axes[1], color='C4')
    axes[1].set_yscale('log')
    axes[1].set_ylabel('Pressure [Pa]')
    
    fig.tight_layout()        