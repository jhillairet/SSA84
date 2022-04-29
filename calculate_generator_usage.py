import pandas as pd
import matplotlib.pyplot as plt
from tresonatordata.pegase import *
from scipy.integrate import trapz, cumtrapz

plt.rcParams['toolbar'] = 'toolmanager'


#%%
files = [
"data/TaskB/pegase/generator_usage_2022-02-14.txt",
"data/TaskB/pegase/generator_usage_2022-02-15.txt",
"data/TaskB/pegase/generator_usage_2022-02-16.txt",
"data/TaskB/pegase/generator_usage_2022-02-17.txt",
"data/TaskB/pegase/generator_usage_2022-03-09.txt",
"data/TaskB/pegase/generator_usage_2022-03-11.txt",
"data/TaskB/pegase/generator_usage_2022-03-14.txt",
"data/TaskB/pegase/generator_usage_2022-03-15.txt",
"data/TaskB/pegase/generator_usage_2022-04-15.txt",
"data/TaskB/pegase/generator_usage_2022-04-19.txt",
"data/TaskB/pegase/generator_usage_2022-04-20.txt",
"data/TaskB/pegase/generator_usage_2022-04-22.txt",
"data/TaskB/pegase/generator_usage_2022-04-21.txt",
"data/TaskB/pegase/generator_usage_2022-04-26.txt",
"data/TaskB/pegase/generator_usage_2022-04-27.txt",
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
