import pandas as pd
import matplotlib.pyplot as plt
from tresonatordata.pegase import *
from scipy.integrate import trapz, cumtrapz

plt.rcParams['toolbar'] = 'toolmanager'


#%% Test contact Arkadia
files = [
"data/TaskB/pegase/generator_usage_2022-08-31.txt",
"data/TaskB/pegase/generator_usage_2022-09-01.txt",
"data/TaskB/pegase/generator_usage_2022-09-02.txt",
"data/TaskB/pegase/generator_usage_2022-09-05.txt",
"data/TaskB/pegase/generator_usage_2022-09-06.txt",
"data/TaskB/pegase/generator_usage_2022-09-07.txt",
"data/TaskB/pegase/generator_usage_2022-09-08.txt",
"data/TaskB/pegase/generator_usage_2022-09-09.txt",
"data/TaskB/pegase/generator_usage_2022-09-13.txt",
"data/TaskB/pegase/generator_usage_2022-09-14.txt",
"data/TaskB/pegase/generator_usage_2022-09-15.txt",
"data/TaskB/pegase/generator_usage_2022-09-16.txt"
    ]
df = load_multiple_pegase_data(files)



#%%
with plt.style.context('seaborn-darkgrid'):
    fig, ax = plt.subplots()
    df.plot(y='Lht1', ax=ax)
    df.plot(y='Lfk1', color='C1', ax=ax)
    fig.tight_layout()

#%%
nb_minutes_HT = df.resample('1min').max()['Lht1'].sum()
nb_minutes_IC = df.resample('1min').max()['Lfk1'].sum()

print(f'{nb_minutes_HT} minutes de HT, soit {nb_minutes_HT/60} heures')
print(f'{nb_minutes_IC} minutes de IC, soit {nb_minutes_IC/60} heures')
