# -*- coding: utf-8 -*-
"""
Plots the summary figures of SSA84 RF tests from resumed parameters.

J.Hillairet, 2022
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['toolbar'] = 'toolmanager'
import hvplot.pandas

#%%
# .reset_index() to allow 'index' as possible axe for scatter plots
df = pd.read_hdf('resumed_parameters_Test2.hdf').reset_index()
df['pulse_nb'] = df.index + 1
# then reapply index as index
df.set_index('index', inplace=True)

# 2022-09-14 Milestone 20 is interrupted by a false positive vacuum interlock
# combine the length of the two points into a unique point
df.loc['2022-09-14 10:39:34.087733', 'pulse_length'] = df.loc['2022-09-14 10:39:34.087733']['pulse_length'] \
                                                        + df.loc['2022-09-14 11:15:48.323114']['pulse_length']
df.drop('2022-09-14 11:15:48.323114', inplace=True)



#%% SWR
df['SWR'] = (1 + np.sqrt(df['Pr_mean']/df['Pi_mean']))/(1 - np.sqrt(df['Pr_mean']/df['Pi_mean']))

#%% SWR vs shot number vs voltage.
with plt.style.context('default'):
    fig, ax = plt.subplots()
    df.plot(kind='scatter', x='pulse_nb', y='SWR', c='V1_mean', cmap='viridis', ax=ax)
    ax.set_xlabel('Pulse #')
    ax.set_ylabel('SWR')
    cbar = plt.gcf().get_axes()[1]  # colorbar instance
    cbar.set_ylabel('V1 mean [V]')        
    fig.autofmt_xdate(rotation=45)
    ax.set_title(f'SSA84 - ARKADIA Contacts')
    ax.set_ylim(bottom=1, top=40)
    fig.tight_layout()

#%% Voltage vs shot number
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots()
    df.plot(y='V1_mean', marker='.', ls='', color='C0', ax=ax)
    df.plot(y='V2_mean', marker='.', ls='', color='C1', ax=ax)
    ax.set_xlabel('Pulse #')
    ax.set_ylabel('Voltage [V]')
    fig.autofmt_xdate(rotation=45)
    ax.set_title(f'SSA84 - ARKADIA Contacts')
    fig.tight_layout()
    fig.savefig(f'SSA84_Test2_voltage_vs_shotnumber.png', dpi=150)

#%% Pulse duration vs shot date
with plt.style.context('default'):
    fig, ax = plt.subplots()
    pressure = np.log10(df[['JR3_max', 'JR4_max']].mean(axis=1))
    df.reset_index().plot(kind='scatter', x='index', y='pulse_length', s=30, c='I_DUT_mean',
                          cmap='plasma', ax=ax, alpha=0.8, clim=(100,2000))
    cbar = plt.gcf().get_axes()[1]  # colorbar instance
    cbar.set_ylabel('Mean DUT Current [A])')    
    ax.set_xlabel('Date')
    ax.set_ylabel('Pulse length [s]')
    ax.set_yscale('log')
    fig.autofmt_xdate(rotation=45)
    ax.set_title(f'SSA84 - ARKADIA Contacts')
    ax.set_ylim(bottom=0.1)
    fig.tight_layout()
    ax.grid(True, which='both', alpha=0.6)
    fig.savefig(f'SSA84_Test2_pulse_length_vs_date.png', dpi=150)
    
    
#%% Pulse duration vs shot number
with plt.style.context('default'):
    fig, ax = plt.subplots()
    df.query('I_DUT_max > 100').plot(ax=ax, kind='scatter', x='pulse_nb', 
                                      y='pulse_length', s=30, c='I_DUT_mean', alpha=0.8, clim=(100,2000))
    cbar = plt.gcf().get_axes()[1]  # colorbar instance
    cbar.set_ylabel('Mean DUT Current [A])')
    ax.set_xlabel('Pulse #')
    ax.set_ylabel('Pulse length [s]')
    ax.set_yscale('log')
    fig.autofmt_xdate(rotation=45)
    ax.set_title(f'SSA84 - ARKADIA Contacts')
    ax.grid(True, which='both', alpha=0.6)
    ax.set_ylim(bottom=0.1)
    fig.tight_layout()
    fig.savefig(f'SSA84_Test2_pulse_length_vs_shotnumber_DUT_current.png', dpi=150)
    
#%% Final Summary
# df.set_index('index')
df['V_mean'] = df[['V1_mean', 'V1_mean']].max(axis=1) / 1e3  # kV
df['Pr/Pi'] = df['Pr_mean']/df['Pi_mean']
df['JR_max'] = df[['JR3_max', 'JR4_max']].max(axis=1)
df['JR_max_log'] = np.log10(df['JR_max'])

# plt.style.use('default')
with plt.style.context('default'):
    fig, ax = plt.subplots()
    _df = df.query('pulse_length > 0.1 and JR_max_log < -2.63')
    _df.plot(ax=ax, kind='scatter', x='pulse_length', y='I_DUT_max',  s=30,
             c='JR_max_log', alpha=0.6, cmap=plt.colormaps['viridis'])
    ax.set_xscale('log')
    ax.set_title('SSA84 - TaskB - ARKADIA Contacts - Successful Pulses')
    ax.set_xlabel('Pulse length [s]')
    ax.set_ylabel('DUT Current (max) [A]')
    fig.get_axes()[-1].set_ylabel('Max Pressure (log) [Pa]')
    ax.grid(True, which='both', alpha=0.6)
    
#%% Relationship between current and forward power
# filtering correct mode only
_df = df.query('pulse_length > 0.1 and JR_max_log < -2.63 and Pr_mean < 5000')
x = _df['I_DUT_mean']
y = _df['Pi_mean']
# polynomial fit
p = np.polyfit(x, y, deg=2)

x_pred = np.arange(0,2000, 10).reshape(-1,1)
y_pred = np.polyval(p, x_pred)

fig, ax = plt.subplots()
_df.plot(kind='scatter', ax=ax, x='I_DUT_mean', y='Pi_mean')
ax.plot(x_pred, y_pred)

def I_DUT_to_Pin(I_DUT):
    return np.polyval(p, I_DUT)

def Pin_to_I_DUT(Pin):
    # positive root
    res = [(np.poly1d(p) - _Pin).roots[1] for _Pin in Pin]
    return np.array(res).reshape(-1, 1)


#%% Final Summary with current and forward power y-scales 
# df.set_index('index')
df['V_mean'] = df[['V1_mean', 'V1_mean']].max(axis=1) / 1e3  # kV
df['Pr/Pi'] = df['Pr_mean']/df['Pi_mean']
df['JR_max'] = df[['JR3_max', 'JR4_max']].max(axis=1)
df['JR_max_log'] = np.log10(df['JR_max'])

_df = df.query('pulse_length > 0.1 and JR_max_log < -2.63')

pl = _df['pulse_length'].values.reshape(-1, 1) 
I_DUT = _df['I_DUT_mean'].values.reshape(-1, 1)
Pi = _df['Pi_mean'].values.reshape(-1, 1)
    

# plt.style.use('default')
with plt.style.context('default'):
    fig, ax = plt.subplots(constrained_layout=True)
    _df.plot(ax=ax, kind='scatter', x='pulse_length', y='I_DUT_max',  s=30,
              c='JR_max_log', alpha=0.6, cmap=plt.colormaps['viridis'])

    # ax.scatter(pl, I_DUT)

    ax.set_xscale('log')
    ax.set_title('SSA84 - TaskB - Arkadia Contacts - Successful Pulses')
    ax.set_xlabel('Pulse length [s]')
    ax.set_ylabel('DUT Current (max) [A]')
    fig.get_axes()[-1].set_ylabel('Max Pressure (log) [Pa]')
    ax.grid(True, which='both', alpha=0.6)

    
    secax = ax.secondary_yaxis(-0.2, functions=(I_DUT_to_Pin, Pin_to_I_DUT))
    secax.set_ylabel('Forward Power [W]')