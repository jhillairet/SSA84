import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from nptdms import TdmsFile

# Allows copy/paste to clipboard using crtl+c command
plt.rcParams['toolbar'] = 'toolmanager'

class TResonatorData():
    def __init__(self, tdms_filename:str):
        '''
        T-Resonator data 

        Parameters
        ----------
        tdms_filename : str
            path to a .tdms file

        Returns
        -------
        data : TResonatorData object 

        '''
        # raw data are store in an internal dictionnary
        self._raw_data = {}
        
        self.fMHz = float(tdms_filename.split('_')[-1].split('.')[0].replace(',', '.').strip('M').strip('F'))
    
        try:
            print(f'Reading {tdms_filename} data... please wait...')
            # The TdmsFile.read method reads all data into memory immediately. 
            # For large TDMS files, TdmsFile.open is more memory efficient but slower
            # with TdmsFile.open(tdms_filename) as tdms_file:
            tdms_file = TdmsFile.read(tdms_filename)    
            for group in tdms_file.groups():
                #group_name = group.name    
                    
                for channel in tqdm(group.channels()):
                    channel_name = channel.name
                    # Access dictionary of properties:
                    properties = channel.properties
                    # Access numpy array of data for channel:
                    self.raw_data[channel_name + '_raw'] = channel[:]
            
            ## load calibration for filters
            # self._filter_calib=pd.read_csv('calibration_filtres_TWA.csv',sep=';',decimal=',')
            # print('Calibration for filters loaded')
            
            ## time properties
            self._raw_data['start_time'] = properties['wf_start_time']    
            self._raw_data['time_step'] = properties['wf_increment']  # time step
            
            # convert raw_data into a pandas DataFrame
            self._df = pd.DataFrame(self.raw_data)
            # time delta is assumed constant
            dt = pd.Timedelta(value=self._raw_data['time_step'], unit='seconds')
            
            # for absolute and relative time vectors
            time_absolute, time_relative = [], []
            for idx in range(len(self._df)):
                time_absolute.append(self.raw_data['start_time'] + idx*dt)
                time_relative.append(idx * dt)
            self._df['time_absolute'] = time_absolute
            self._df['time'] = time_relative
            self._df['fMHz'] = self.fMHz
            self._df.set_index('time', inplace=True)
            self._df['time_seconds'] = self._df.index.total_seconds() # time in seconds (for plots)
            
            # # Post processing
            # self.raw_TOS_to_RL()
            # self.raw_V_to_V()
            # self.raw_vac_to_vac()
            # self.raw_Piout_to_Piout()
            # self.raw_Piin_to_Piin()
            # self.raw_Pgen_to_Pgen()
            # self.raw_Tc_to_Tc()
            # self.raw_Vm_to_Pm()

        except Exception as e: # hu ho...
            print(e)

    def __repr__(self) -> str:
        '''
        Object description
        '''
        return f'TWA mockup data object ({self.fMHz} MHz). .df property contains: \n' + \
            str(self.df.columns.to_list())

    @property
    def df(self) -> pd.DataFrame:
        '''
        Return TDMS data as a pandas DataFrame object

        Returns
        -------
        df : pandas DataFrame
            TDMS data and relative and absolute time

        '''
        return self._df
    
    @property
    def raw_data(self) -> dict:
        '''
        Raw data as a dictionnary

        Returns
        -------
        raw_data : dict
            raw data

        '''
        return self._raw_data
  