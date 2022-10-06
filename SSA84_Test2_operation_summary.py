#%%
import pandas as pd
import matplotlib.pyplot as plt
from tresonatordata.pegase import load_multiple_pegase_data
import numpy as np

plt.rcParams['toolbar'] = 'toolmanager'

# Tests Arkadia

#%% Baking phase
files = [
"data/TaskB/pegase/continuous_data_2022-07-13_2022-09-19.txt",
"data/TaskB/pegase/continuous_data_2022-08-30_2022-09-19.txt"
]

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 150] = np.NaN
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
    axes[1].set_ylim(top=1e-2, bottom=2e-5)
    # 13/07/2022 -> 27/07/2022
    axes[1].set_xlim(19186.005926712984, 19200.951829871556)
    fig.tight_layout()


#%% RF Tests
files = [
"data/TaskB/pegase/continuous_data_2022-08-30_2022-09-19.txt"
]

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 100] = np.NaN
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
    axes[1].set_ylim(top=1e-2, bottom=1e-5)
    # # 13/07/2022 -> 27/07/2022
    # axes[1].set_xlim(19186.005926712984, 19200.951829871556)
    fig.tight_layout()

#%% RF Tests with better resolution
files = [
"data/TaskB/pegase/continuous_data_2022-08-30.txt",
"data/TaskB/pegase/continuous_data_2022-08-31.txt",
"data/TaskB/pegase/continuous_data_2022-09-01.txt",
"data/TaskB/pegase/continuous_data_2022-09-02.txt",
"data/TaskB/pegase/continuous_data_2022-09-03.txt",
"data/TaskB/pegase/continuous_data_2022-09-04.txt",
"data/TaskB/pegase/continuous_data_2022-09-05.txt",
"data/TaskB/pegase/continuous_data_2022-09-06.txt",
"data/TaskB/pegase/continuous_data_2022-09-07.txt",
"data/TaskB/pegase/continuous_data_2022-09-08.txt",
"data/TaskB/pegase/continuous_data_2022-09-09.txt",
"data/TaskB/pegase/continuous_data_2022-09-10.txt",
"data/TaskB/pegase/continuous_data_2022-09-11.txt",
"data/TaskB/pegase/continuous_data_2022-09-12.txt",
"data/TaskB/pegase/continuous_data_2022-09-13.txt",
"data/TaskB/pegase/continuous_data_2022-09-14.txt",
"data/TaskB/pegase/continuous_data_2022-09-15.txt",
"data/TaskB/pegase/continuous_data_2022-09-16.txt"
]

df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 100] = np.NaN
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
    axes[1].set_ylim(top=1e-2, bottom=1e-5)
    # # 13/07/2022 -> 27/07/2022
    # axes[1].set_xlim(19186.005926712984, 19200.951829871556)
    fig.tight_layout()