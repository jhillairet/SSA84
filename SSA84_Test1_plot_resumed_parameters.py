# -*- coding: utf-8 -*-
"""
Plots the summary figures of SSA84 RF tests from resumed parameters.

J.Hillairet, 2022
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['toolbar'] = 'toolmanager'

#%%
# .reset_index() to allow 'index' as possible axe for scatter plots
df_part1 = pd.read_hdf('resumed_parameters_part1.hdf').reset_index()
df_part2 = pd.read_hdf('resumed_parameters_part2.hdf').reset_index()
df_part3 = pd.read_hdf('resumed_parameters_part3.hdf').reset_index()
# generate pulse numbers
df_part1['pulse_nb'] = df_part1.index + 1
df_part2['pulse_nb'] = df_part2.index + 1
df_part3['pulse_nb'] = df_part3.index + 1

#%% SWR
for part_number, df in enumerate([df_part1, df_part2, df_part3]):
    df['SWR'] = (1 + np.sqrt(df['Pr_mean']/df['Pi_mean']))/(1 - np.sqrt(df['Pr_mean']/df['Pi_mean']))

#%% SWR vs shot number vs voltage.
for part_number, df in enumerate([df_part1, df_part2, df_part3]):
    with plt.style.context('default'):
        fig, ax = plt.subplots()
        df.plot(kind='scatter', x='pulse_nb', y='SWR', c='V1_mean', cmap='viridis', ax=ax)
        ax.set_xlabel('Pulse #')
        ax.set_ylabel('SWR')
        cbar = plt.gcf().get_axes()[1]  # colorbar instance
        cbar.set_ylabel('V1 mean [V])')        
        fig.autofmt_xdate(rotation=45)
        ax.set_title(f'SSA84 - Part {part_number+1}')
        ax.set_ylim(bottom=1, top=40)
        fig.tight_layout()

#%% Voltage vs shot number
for part_number, df in enumerate([df_part1, df_part2, df_part3]):
    with plt.style.context('default'):
        fig, ax = plt.subplots()
        df.plot(y='V1_mean', marker='.', ls='', color='C0', ax=ax)
        df.plot(y='V2_mean', marker='.', ls='', color='C1', ax=ax)
        ax.set_xlabel('Pulse #')
        ax.set_ylabel('Voltage [V]')
        fig.autofmt_xdate(rotation=45)
        ax.set_title(f'SSA84 - Part {part_number+1}')
        fig.tight_layout()
        fig.savefig(f'SSA84_Part{part_number+1}_voltage_vs_shotnumber.png', dpi=150)

#%% Pulse duration vs shot number
for part_number, df in enumerate([df_part1, df_part2, df_part3]):
    with plt.style.context('default'):
        fig, ax = plt.subplots()
        pressure = np.log10(df[['JR3_max', 'JR4_max']].mean(axis=1))
        df.plot(kind='scatter', x='pulse_nb', y='pulse_length', s=30, c=pressure, cmap='viridis', ax=ax, alpha=0.8)
        cbar = plt.gcf().get_axes()[1]  # colorbar instance
        cbar.set_ylabel('log10(p) (p in [Pa])')
        ax.set_xlabel('Pulse #')
        ax.set_ylabel('Pulse length [s]')
        ax.set_yscale('log')
        fig.autofmt_xdate(rotation=45)
        ax.set_title(f'SSA84 - Part {part_number+1}')
        fig.tight_layout()
        fig.savefig(f'SSA84_Part{part_number+1}_pulse_length_vs_shotnumber.png', dpi=150)
    
    
    #%% Pulse duration vs shot number
    for part_number, df in enumerate([df_part1, df_part2, df_part3]):
        with plt.style.context('default'):
            fig, ax = plt.subplots()
            pressure = np.log10(df[['JR3_max', 'JR4_max']].mean(axis=1))
            df.plot(kind='scatter', x='pulse_nb', y='pulse_length', s=30, c='V1_mean', cmap='viridis', ax=ax, alpha=0.8)
            cbar = plt.gcf().get_axes()[1]  # colorbar instance
            cbar.set_ylabel('log10(p) (p in [Pa])')
            ax.set_xlabel('Pulse #')
            ax.set_ylabel('Pulse length [s]')
            ax.set_yscale('log')
            fig.autofmt_xdate(rotation=45)
            ax.set_title(f'SSA84 - Part {part_number+1}')
            fig.tight_layout()
            #fig.savefig(f'SSA84_Part{part_number+1}_pulse_length_vs_shotnumber_voltage.png', dpi=150)
    
# %%
# with plt.style.context('default'):
#     fig, ax = plt.subplots()
#     df_part1.plot()
#     ax.plot( np.min([JR3_mmm[:,2], JR4_mmm[:,2]], axis=0), '.', color='C0', label='shot start pressure', alpha=0.4)
#     ax.plot(np.max([JR3_mmm[:,3], JR4_mmm[:,3]], axis=0), '.', color='C1', label='max pressure during shot', alpha=0.4)
#     ax.set_yscale('log')
#     ax.legend()
#     ax.set_xlabel('day shot #')
#     ax.set_ylabel('pressure [Pa]')
#     ax.set_title('SSA84 - Part 1')
    
#%% tests
fig, ax = plt.subplots()
df_part1['JR_max'] = df_part1[['JR3_max', 'JR4_max']].max(axis=1)
df_part1['V_max'] = df_part1[['V1_max', 'V1_max']].max(axis=1)
df_part1['Pr/Pi'] = df_part1['Pr_mean']/df_part1['Pi_mean']
df_part1['test'] = df_part1['V1_mean']*df_part1['pulse_length']
df_part1.plot(kind='scatter', x='pulse_nb', y='Pr/Pi', ax=ax, s=30, c='V_max', cmap='viridis', alpha=0.5)
ax.set_yscale('log')

#%%
fig, ax = plt.subplots()
df_part2['JR_max'] = df_part2[['JR3_max', 'JR4_max']].max(axis=1)
df_part2['V_max'] = df_part2[['V1_mean', 'V1_mean']].max(axis=1)
df_part2['Pr/Pi'] = df_part2['Pr_mean']/df_part2['Pi_mean']
df_part2['test'] = df_part2['V1_mean']*df_part2['pulse_length']
df_part2.plot(kind='scatter', x='pulse_nb', y='Pr/Pi', ax=ax, s=30, c='V_max', cmap='viridis', alpha=0.5, vmax=5e3)

#%% Final Summary
df = pd.concat([df_part1, df_part2, df_part3])
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
    ax.set_title('SSA84 - TaskB - Stäubli Contacts - Successful Pulses')
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
df = pd.concat([df_part1, df_part2, df_part3])
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
    ax.set_title('SSA84 - TaskB - Stäubli Contacts - Successful Pulses')
    ax.set_xlabel('Pulse length [s]')
    ax.set_ylabel('DUT Current (max) [A]')
    fig.get_axes()[-1].set_ylabel('Max Pressure (log) [Pa]')
    ax.grid(True, which='both', alpha=0.6)

    
    secax = ax.secondary_yaxis(-0.2, functions=(I_DUT_to_Pin, Pin_to_I_DUT))
    secax.set_ylabel('Forward Power [W]')