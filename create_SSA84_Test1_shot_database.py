# -*- coding: utf-8 -*-
"""
Create a resumed database of the SSA84 TaskB RF tests.

J.Hillairet, 2022
"""
from glob import glob
from tresonatordata.tresonatordata import *
from os.path import join

#%%
def hdf_files(directories):
    # keep only .hdf files
    hdf_files = []
    for directory in directories:
        name_filter = join(directory, '*.hdf')
        hdf_files.extend(glob(name_filter))
    return hdf_files

#%% Part 1
directories = [
    'E:\SSA84\data/2022-02-02_SSA84_RF_tests', # Part 1
    'E:\SSA84\data/2022-02-03_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-04_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-14_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-15_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-16_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-17_SSA84_RF_tests',
    ]
db_part1 = create_resumed_parameters(hdf_files(directories))
db_part1.to_hdf('resumed_parameters_part1.hdf', key='part1')

#%%
directories = [
    'E:\SSA84\data/2022-03-11_SSA84_RF_tests', # Part 2   
    'E:\SSA84\data/2022-03-14_SSA84_RF_tests',
    'E:\SSA84\data/2022-03-15_SSA84_RF_tests',  
    ]
db_part2 = create_resumed_parameters(hdf_files(directories))
db_part2.to_hdf('resumed_parameters_part2.hdf', key='part2')

#%%
directories = [
    'E:\SSA84\data/2022-04-15_SSA84_RF_tests', # Part 3   
    'E:\SSA84\data/2022-04-19_SSA84_RF_tests',  
    'E:\SSA84\data/2022-04-20_SSA84_RF_tests',
    'E:\SSA84\data/2022-04-21_SSA84_RF_tests',
    'E:\SSA84\data/2022-04-22_SSA84_RF_tests',
    'E:\SSA84\data/2022-04-26_SSA84_RF_tests',
    'E:\SSA84\data/2022-04-27_SSA84_RF_tests',  
    ]
db_part3 = create_resumed_parameters(hdf_files(directories))
db_part3.to_hdf('resumed_parameters_part3.hdf', key='part3')