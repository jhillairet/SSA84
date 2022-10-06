# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:13 2022

@author: JH218595
"""
import matplotlib.pyplot as plt
from tresonatordata.tresonatordata import TResonatorData, create_resumed_parameters
import pandas as pd
from os.path import join

# basedir = "V:\\Projets\\ICRH system for ITER\\IO_SSA_84 R&D ICRH Antenna\\6. Internal documents\\Task B RF Contacts\\RF Tests Data\\data\\2022-09-13_SSA84_RF_tests/"

file = "data/2022-09-13_SSA84_RF_tests/WRF_2022-09-13_13-52-23_F61,710000M.hdf"
data = TResonatorData(file)

#%% Milestone 17
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
    ax[0].set_xlim(103609187966.52226, 176786228917.7932)
    # fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig('SSA84_ARKADIA_milestone17.png', dpi=150)

#%% Milestone 18
file = "data/2022-09-13_SSA84_RF_tests/WRF_2022-09-13_13-56-50_F61,710000M.hdf"
data = TResonatorData(file)

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
    fig.savefig('SSA84_ARKADIA_milestone18.png', dpi=150)
    
#%% Milestone 19
file = "data/2022-09-13_SSA84_RF_tests/WRF_2022-09-13_15-12-17_F61,710000M.hdf"
data = TResonatorData(file)

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
    fig.savefig('SSA84_ARKADIA_milestone19.png', dpi=150)

    