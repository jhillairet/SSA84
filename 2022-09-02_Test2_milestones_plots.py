# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:13 2022

@author: JH218595
"""
import matplotlib.pyplot as plt
from tresonatordata.tresonatordata import TResonatorData
import pandas as pd
from os.path import join

basedir = "V:\\Projets\\ICRH system for ITER\\IO_SSA_84 R&D ICRH Antenna\\6. Internal documents\\Task B RF Contacts\\RF Tests Data\\data\\2022-09-02_SSA84_RF_tests/"


#%% Milestone 4
file = join(basedir, 'WRF_2022-09-02_11-43-53_F62,334000M.hdf')
data = TResonatorData(file)

with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots(5, 1, sharex=True, layout='compressed')
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
    ax[0].set_xlim(282647653225.80646, 366504723118.2796)
    fig.savefig('SSA84_ARKADIA_milestone4.png', dpi=150)

    
#%% Milestone 5
file = join(basedir, 'WRF_2022-09-02_13-01-10_F62,334000M.hdf')
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
    # ax[0].set_xlim(310481401209.67737, 488885000000.0)
    fig.savefig('SSA84_ARKADIA_milestone5.png', dpi=150)
    