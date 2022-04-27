# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:13 2022

@author: JH218595
"""
import matplotlib.pyplot as plt
import pyqtgraph as pg
from tresonatordata.tresonatordata import TResonatorData
import pandas as pd


#%%
data = TResonatorData('data/2022-03-14_SSA84_RF_tests/WRF_2022-03-14_17-44-47_F61,850000M.hdf')
data2 = TResonatorData('data/2022-03-14_SSA84_RF_tests/WRF_2022-03-14_17-54-47_F61,850000M.hdf')
data2.df.index + data.df.index[-1]
data._df = pd.concat([data.df, data2.df])

#%%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    # fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig('SSA84_milestone6_part2.png', dpi=150)

#%% Milestone 8: 5 x 1s @ 1kA
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_10-39-35_F61,820000M.hdf')

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()
    # fig.savefig('SSA84_milestone8_part2.png', dpi=150)

#%% Milestone 9: 5 x 2s @ 1kA
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_11-49-37_F61,860000M.hdf')

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()
    # fig.savefig('SSA84_milestone8_part2.png', dpi=150)

#%% Milestone 10: 5 x 5s @ 1kA
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_13-17-44_F61,835000M.hdf')

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()
    # fig.savefig('SSA84_milestone10_part2.png', dpi=150)

#%% Milestone 11: 5 x 10s @ 1kA
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_13-29-46_F61,835000M.hdf')

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()
    # fig.savefig('SSA84_milestone11_part2.png', dpi=150)
    
#%% Milestone 12: 5 x 60s @ 1kA, 3 first attemps
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_14-24-54_F61,835000M.hdf')
data2 = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_14-34-55_F61,835000M.hdf')
data2.df.index + data.df.index[-1]
data._df = pd.concat([data.df, data2.df])

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()
    # fig.savefig('SSA84_milestone12_part2.png', dpi=150)
    
#%% Milestone 12: 5 x 60s @ 1kA, 4th attemps
data = TResonatorData('data/2022-03-15_SSA84_RF_tests/WRF_2022-03-15_15-45-16_F61,835000M.hdf')

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    data.df.plot(y='Pi [W]', ax=ax[0])
    data.df.plot(y='Pr [W]', ax=ax[0])
    
    data.df.plot(y='V1 [V]', ax=ax[1])
    data.df.plot(y='V2 [V]', ax=ax[1])
    
    data.df.plot(y='I_CEA_max', ax=ax[2])
    data.df.plot(y='I_DUT_max', ax=ax[2])
    
    data.df.plot(y='JR3', ax=ax[3])
    data.df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    data.df.plot(y='TC1', ax=ax[4])
    data.df.plot(y='TC2', ax=ax[4])
    data.df.plot(y='TC3', ax=ax[4])
    data.df.plot(y='TC4', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.tight_layout()