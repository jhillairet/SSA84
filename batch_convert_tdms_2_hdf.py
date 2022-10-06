# -*- coding: utf-8 -*-
"""
Batch conversion of the raw data (.tdms) from Labview to processed data (.hdf)
"""

from glob import glob
from tresonatordata.tresonatordata import TResonatorData
from tqdm import tqdm
from os.path import dirname, abspath, join, exists

directories = [
    # 'data/2022-02-02_SSA84_RF_tests',  # part 1
    # 'data/2022-02-03_SSA84_RF_tests',
    # 'data/2022-02-04_SSA84_RF_tests',
    # 'data/2022-02-14_SSA84_RF_tests',
    # 'data/2022-02-15_SSA84_RF_tests',
    # 'data/2022-02-16_SSA84_RF_tests',
    # 'data/2022-02-17_SSA84_RF_tests',
    # 'data/2022-03-11_SSA84_RF_tests',  # part 2
    # 'data/2022-03-14_SSA84_RF_tests',
    # 'data/2022-03-15_SSA84_RF_tests',
    # 'data/2022-04-15_SSA84_RF_tests',  # part 3
    # 'data/2022-04-19_SSA84_RF_tests',
    # 'data/2022-04-20_SSA84_RF_tests',
    # 'data/2022-04-21_SSA84_RF_tests',
    # 'data/2022-04-22_SSA84_RF_tests',
    # 'data/2022-04-26_SSA84_RF_tests',
    # 'data/2022-04-27_SSA84_RF_tests',  
    # 'data/2022-08-31_SSA84_RF_tests/',   
    'data/2022-09-08_SSA84_RF_tests/',       
    'data/2022-09-13_SSA84_RF_tests/',       
    ]

# get all .tdms files in all directories
tdms_files = []
for directory in directories:
    name_filter = join(dirname(abspath(__file__)), directory, '*.tdms')
    tdms_files.extend(glob(name_filter))

# convert all .tdms files to HDF
for tdms_file in tqdm(tdms_files):
    hdf_file = tdms_file.replace('tdms', 'hdf')
    # do not convert if the file already exist
    if not exists(hdf_file):
        try:
            data = TResonatorData(tdms_file)
            data.to_hdf(hdf_file)
            del data
        except AttributeError as e:
            print(f'Error in reading file {tdms_file}. Skipping...')