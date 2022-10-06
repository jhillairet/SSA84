#%%
import pandas as pd
import matplotlib.pyplot as plt
from tresonatordata.pegase import load_multiple_pegase_data
import numpy as np

plt.rcParams['toolbar'] = 'toolmanager'

#%% 
files = [
    "data/TaskB/pegase/continuous_data_2022-02-28-06.txt",
    "data/TaskB/pegase/continuous_data_2022-03-07-10.txt",
    "data/TaskB/pegase/continuous_data_2022-03-11.txt",
    "data/TaskB/pegase/continuous_data_2022-03-12-13.txt",
    "data/TaskB/pegase/continuous_data_2022-03-14.txt",
    "data/TaskB/pegase/continuous_data_2022-03-15.txt",
    "data/TaskB/pegase/continuous_data_2022-03-16.txt"]

df = load_multiple_pegase_data(files)

#%%
df['R_TB70'] = df[['R_TCA', 'R_TCB', 'R_TCC',
                   'R_TCD', 'R_TCE', 'R_TCG']].mean(axis=1)
# filter unphysical points
df['R_TB70'][df['R_TB70'] > 300] = np.NaN
df['R_TCF'][df['R_TCF'] > 300] = np.NaN

# missing measurements
df['R_TCF'][df.index < '2022-03-09'] = np.NaN

#%%
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
    
    