# -*- coding: utf-8 -*-
"""
Create a resumed database of the SSA84 TaskB RF tests.
"""
from glob import glob
from tresonatordata.tresonatordata import *
from tqdm import tqdm
from os.path import dirname, abspath, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
directories = [
    'E:\SSA84\data/2022-02-02_SSA84_RF_tests', # Part 1
    'E:\SSA84\data/2022-02-03_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-04_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-14_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-15_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-16_SSA84_RF_tests',
    'E:\SSA84\data/2022-02-17_SSA84_RF_tests',
    ]

# keep only .hdf files
hdf_files = []
for directory in directories:
    name_filter = join(dirname(abspath(__file__)), directory, '*.hdf')
    hdf_files.extend(glob(name_filter))

db_part1 = create_resumed_parameters(hdf_files)



