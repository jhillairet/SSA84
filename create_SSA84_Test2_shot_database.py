# -*- coding: utf-8 -*-
"""
Create a resumed database of the SSA84 TaskB RF tests.

J.Hillairet, 2022
"""
from glob import glob
from tresonatordata.tresonatordata import create_resumed_parameters
from os.path import join

basedir = "V:\\Projets\\ICRH system for ITER\\IO_SSA_84 R&D ICRH Antenna\\6. Internal documents\\Task B RF Contacts\\RF Tests Data\\data\\"

#%%
def hdf_files(directories):
    # keep only .hdf files
    hdf_files = []
    for directory in directories:
        name_filter = join(directory, '*.hdf')
        hdf_files.extend(glob(name_filter))
    return hdf_files

#%% Part 1
subdirectories = [
    '2022-08-31_SSA84_RF_tests',
    '2022-09-01_SSA84_RF_tests',
    '2022-09-02_SSA84_RF_tests',
    '2022-09-06_SSA84_RF_tests',
    '2022-09-07_SSA84_RF_tests',
    '2022-09-08_SSA84_RF_tests',
    '2022-09-09_SSA84_RF_tests',
    '2022-09-12_SSA84_RF_tests',
    '2022-09-13_SSA84_RF_tests',    
    '2022-09-14_SSA84_RF_tests',
    '2022-09-15_SSA84_RF_tests',
    '2022-09-16_SSA84_RF_tests',    
    ]
directories = [join(basedir, _dir) for _dir in subdirectories]

db_arkadia = create_resumed_parameters(hdf_files(directories))

#%% Manual corrections of the resumed data 
# some points must be corrected, for example to combine long shots 
# interrupted by a false positive vacuum interlock

# 2022-09-14 Milestone 20 is interrupted by a false positive vacuum interlock
# combine the length of the two points into a unique point
db_arkadia.loc['2022-09-14 11:15:48.323114']['pulse_length'] += db_arkadia.loc['2022-09-14 11:53:41.578114']['pulse_length']
db_arkadia.drop('2022-09-14 11:53:41.578114', inplace=True)


#%% Saving database
db_arkadia.to_hdf('resumed_parameters_Test2.hdf', key='part1')
