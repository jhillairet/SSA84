import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tresonatordata.pegase import load_multiple_pegase_data

plt.rcParams['toolbar'] = 'toolmanager'


#%%
files = [
    "data/TaskB/pegase/continuous_data_2022-04-05.txt",
    "data/TaskB/pegase/continuous_data_2022-04-06.txt",
    "data/TaskB/pegase/continuous_data_2022-04-07.txt",
    "data/TaskB/pegase/continuous_data_2022-04-08-13.txt",
    "data/TaskB/pegase/continuous_data_2022-04-14.txt",
    "data/TaskB/pegase/continuous_data_2022-04-15.txt",
    "data/TaskB/pegase/continuous_data_2022-04-16-17.txt",
    "data/TaskB/pegase/continuous_data_2022-04-18.txt",
    "data/TaskB/pegase/continuous_data_2022-04-19.txt",
    "data/TaskB/pegase/continuous_data_2022-04-20.txt",
    "data/TaskB/pegase/continuous_data_2022-04-21.txt",
    "data/TaskB/pegase/continuous_data_2022-04-22.txt",
    # "data/TaskB/pegase/continuous_data_2022-04-23-25.txt",
    "data/TaskB/pegase/continuous_data_2022-04-26.txt",
    "data/TaskB/pegase/continuous_data_2022-04-27.txt" 
    ]
df = load_multiple_pegase_data(files)

df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)

#%% filter spurious points < 1e-6 Pa (JR3)
df['R_JR3'][df['R_JR3'] < 1e-5] = np.NaN
df['R_JR4'][df['R_JR4'] < 1e-5] = np.NaN

#%% filter spurious B70 temperature (>80°C??)
df['R_TB70'][df['R_TB70'] > 80] = np.NaN

# missing measurements
df['R_TCF'][df.index < '2022-04-19 13:57'] = np.NaN

#%%
with plt.style.context('seaborn-darkgrid'):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12.5, 5.5))
    df.plot(y='R_TB70', ax=axes[0], label='Resonator (B70 avg)')
    df.plot(y='R_TCF', ax=axes[0], label='DUT (B500)', color='C3')
    axes[0].set_ylabel('Temperature [°C]')
    
    df.plot(y='R_JR3', ax=axes[1], color='C1')
    df.plot(y='R_JR4', ax=axes[1], color='C4')
    axes[1].set_yscale('log')
    axes[1].set_ylabel('Pressure [Pa]')

    fig.tight_layout()

#%%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(sharex=True)
    df.plot(y='R_JR3', ax=ax)
    df.plot(y='R_JR4', ax=ax)
    ax.set_yscale('log')
    ax.set_ylabel('Pressure [Pa]')
    ax.set_ylim(top=0.1)
    fig.tight_layout()
