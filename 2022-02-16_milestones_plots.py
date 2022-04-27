# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:03:13 2022

@author: JH218595
"""
import matplotlib.pyplot as plt
import pyqtgraph as pg
from tresonatordata.tresonatordata import TResonatorData



#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-42-43_F61,735000M.tdms')
# data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-51-29_F61,735000M.tdms')
# data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-56-11_F61,735000M.tdms')

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
fig.autofmt_xdate(rotation=45)
fig.savefig('SSA84_milestone6.png', dpi=150)

#%%
data = TResonatorData('data/2022-02-17_SSA84_RF_tests/WRF_2022-02-17_09-18-31_F61,740000M.hdf')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.autofmt_xdate(rotation=45)
fig.savefig('SSA84_milestone5_tentative.png', dpi=150)


#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-38-52_F61,735000M.tdms')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.autofmt_xdate(rotation=45)
ax[-1].set_xlim(57159925403.225815, 195462961693.5484)
fig.savefig('SSA84_milestone5.png', dpi=150)

#%%
data = TResonatorData('data/2022-02-17_SSA84_RF_tests/WRF_2022-02-17_09-05-51_F61,740000M.hdf')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.autofmt_xdate(rotation=45)
fig.tight_layout()
fig.savefig('SSA84_milestone4_2.png', dpi=150)



#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-37-19_F61,735000M.tdms')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.autofmt_xdate(rotation=45)
fig.savefig('SSA84_milestone4.png', dpi=150)

#%%
ax[-1].set_xlim((29325100806.451614, 34251717741.935486))
fig.savefig('SSA84_milestone4_zoom.png', dpi=150)


#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_17-58-52_F61,735000M.tdms')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.savefig('SSA84_milestone3.png', dpi=150)

#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_17-56-48_F61,735000M.tdms')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
# ax[-1].set_xlim((32896766869.40738, 60115865681.622765))
fig.autofmt_xdate(rotation=45)
fig.tight_layout()
fig.savefig('SSA84_milestone2.png', dpi=150)
#%%
ax[-1].set_xlim((52810749457.39733, 54197577406.94179))
fig.savefig('SSA84_milestone2_zoom.png', dpi=150)

#%%
data = TResonatorData('data/2022-02-16_SSA84_RF_tests/WRF_2022-02-16_18-19-12_F61,735000M.tdms')

fig, ax = plt.subplots(4, 1, sharex=True)
data.df.plot(y='Pi [W]', ax=ax[0])
data.df.plot(y='Pr [W]', ax=ax[0])

data.df.plot(y='V1 [V]', ax=ax[1])
data.df.plot(y='V2 [V]', ax=ax[1])

data.df.plot(y='I_CEA_max', ax=ax[2])
data.df.plot(y='I_DUT_max', ax=ax[2])

data.df.plot(y='JR3', ax=ax[3])
data.df.plot(y='JR4', ax=ax[3])

ax[3].set_yscale('log')

ax[0].set_title(f'SSA84 - {data.date} - {data.time} - f={data.fMHz} MHz')
fig.autofmt_xdate(rotation=45)
fig.savefig('SSA84_milestone1.png', dpi=150)



#%%
# zoom
ax[0].set_xlim(37884814049.75034, 38109542574.374115)
fig.tight_layout()
fig.savefig('SSA84_milestone1_zoom.png', dpi=150)