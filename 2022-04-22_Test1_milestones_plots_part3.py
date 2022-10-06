# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:13 2022

@author: JH218595
"""
import matplotlib.pyplot as plt
import pyqtgraph as pg
from tresonatordata.tresonatordata import TResonatorData
import pandas as pd


#%% Milestone 14 (5x1.5kA/20ms)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_10-29-09_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 15 (5x1.5kA/1s)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_10-22-04_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 16 (5x1.5kA/2s)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_10-38-36_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 17 (5x1.5kA/5s)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_10-53-05_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 18 (5x1.5kA/10s)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_11-18-17_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 12 (5x1.0kA/60s)

data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_11-35-18_F62,120000.hdf')
data2 = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_11-51-14_F62,120000.hdf')
data3 = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_12-17-25_F62,120000.hdf')
data2.df.index = data2.df.index + data.df.index[-1]
data3.df.index = data3.df.index + data2.df.index[-1]
data._df = pd.concat([data.df, data2.df, data3.df])
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 19 (5x1.5kA/60s)
data = TResonatorData('data/2022-04-22_SSA84_RF_tests/WRF_2022-04-22_14-26-51_F62,120000.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 21 (5x2kA/20ms)
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_09-47-42_F62,040000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)
    
#%% Milestone 22 (5x2kA/1s)
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_09-51-46_F62,040000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)
    
#%% Milestone 23 (5x2kA/2s)
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_11-21-24_F62,040000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Milestone 24 (5x2kA/5s)
data =  TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_12-47-07_F62,040000M.hdf')  # last shot is OK
data2 = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_13-03-27_F62,040000M.hdf')  # 4 shots
data2.df.index = data2.df.index + data.df.index[-1]
data._df = pd.concat([data.df, data2.df])
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)

#%% Essai 1kA/3600s - coupure sur vide après 2 min 
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_13-19-07_F62,040000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)     
    
#%% Essai 1kA/3600s - coupure sur vide après 10 min 
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_13-35-26_F62,041000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)      

#%% Essais de réapplication de la puissance -> échecs (flashs à la vidéo)
data = TResonatorData('data/2022-04-26_SSA84_RF_tests/WRF_2022-04-26_15-40-47_F62,041000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)   

#%% Lendemain, essais RF -> flashs
data = TResonatorData('data/2022-04-27_SSA84_RF_tests/WRF_2022-04-27_09-56-48_F62,050000M.hdf')
df= data.df

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True)
    df.plot(y='Pi [W]', ax=ax[0])
    df.plot(y='Pr [W]', ax=ax[0])
    
    df.plot(y='V1 [V]', ax=ax[1])
    df.plot(y='V2 [V]', ax=ax[1])
    
    df.plot(y='I_CEA_max', ax=ax[2])
    df.plot(y='I_DUT_max', ax=ax[2])
    
    df.plot(y='JR3', ax=ax[3])
    df.plot(y='JR4', ax=ax[3])
    
    ax[3].set_yscale('log')
    
    df.plot(y='TC1_smooth', ax=ax[4])
    df.plot(y='TC2_smooth', ax=ax[4])
    df.plot(y='TC3_smooth', ax=ax[4])
    df.plot(y='TC4_smooth', ax=ax[4])
    
    ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
    fig.autofmt_xdate(rotation=45)   

    