import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from tqdm import tqdm
from nptdms import TdmsFile
from scipy.interpolate import interp1d
from os.path import exists

# Allows copy/paste to clipboard using crtl+c command
plt.rcParams['toolbar'] = 'toolmanager'

class TResonatorData():
    def __init__(self, filename:str):
        '''
        T-Resonator data 

        Parameters
        ----------
        filename : str
            path to a .tdms or a .hdf file

        Returns
        -------
        data : TResonatorData object 

        '''
        if not exists(filename):
            raise FileNotFoundError(f'file {filename} not found!')
        
        # calibration directory
        self.cal_dir = os.path.dirname(os.path.abspath(__file__))+'/calibrations/'
        
        # raw data are store in an internal dictionnary
        self._raw_data = {}

        # extract frequency and date from filename        
        self.fMHz = float(filename.split('_')[-1].split('.')[0].replace(',', '.').strip('M').strip('F'))
        self.date = filename.split('/')[-1].split('_')[1]
        self.time = filename.split('/')[-1].split('_')[2]
    
        try:
            print(f'Reading {filename} data... please wait...')
            
            extension = filename.split('.')[-1]
            
            if extension == 'tdms':
                # The TdmsFile.read method reads all data into memory immediately. 
                # For large TDMS files, TdmsFile.open is more memory efficient but slower
                # with TdmsFile.open(tdms_filename) as tdms_file:
                tdms_file = TdmsFile.read(filename)    
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
                self.raw_V_to_Vprobe()
                self.Vprobe_to_Vmax_and_Imax()
                self.raw_P_to_P()
                self.raw_Vac_to_Vac()
                self.raw_Tc_to_Tc()

            # HDF file. 
            # These files have already been post-processed from TDMS raw data.
            elif extension == 'hdf':
                self._df = pd.read_hdf(filename)

            else:
                raise ValueError('Unknown file type.')

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
  
    def raw_P_to_P(self):
        """
        Process the raw power signals.
        
        The results are power in watts
        """
        cal_Pi = pd.read_csv(self.cal_dir+'SSA84_TaskB_calibration_Pi.csv', sep=';')
        cal_Pr = pd.read_csv(self.cal_dir+'SSA84_TaskB_calibration_Pr.csv', sep=';')
        # takes the calibration coefficients the closest to the gene frequency
        closest_Pi = cal_Pi.iloc[(cal_Pi['f [MHz]'] - self.fMHz).abs().argsort()][:1]
        closest_Pr = cal_Pr.iloc[(cal_Pr['f [MHz]'] - self.fMHz).abs().argsort()][:1]
        # dB -> W
        self._df['Pi [W]'] = 10**((closest_Pi['a'].values*self._df['Pi_raw'] + closest_Pi['b'].values + closest_Pi['att'].values)/10.0)/1e3
        self._df['Pr [W]'] = 10**((closest_Pr['a'].values*self._df['Pr_raw'] + closest_Pr['b'].values + closest_Pr['att'].values)/10.0)/1e3
        # Return Loss at generator
        self._df['RL [dB]'] = 10*np.log10(self._df['Pr [W]']/self._df['Pi [W]'])
  
    def raw_V_to_Vprobe(self):
        '''
        Process the raw probe voltage signals.
        
        The results are voltage in Volt.
        '''
        ## calibration data
        cal_V1 = pd.read_csv(self.cal_dir+'SSA84_TaskB_VoltageProbeV1.csv', sep=';')
        cal_V2 = pd.read_csv(self.cal_dir+'SSA84_TaskB_VoltageProbeV2.csv', sep=';')
        cal_V3 = pd.read_csv(self.cal_dir+'SSA84_TaskB_VoltageProbeV3.csv', sep=';')
        # takes the calibration coefficients the closest to the gene frequency
        closest_V1 = cal_V1.iloc[(cal_V1['f [MHz]'] - self.fMHz).abs().argsort()][:5]
        closest_V2 = cal_V2.iloc[(cal_V2['f [MHz]'] - self.fMHz).abs().argsort()][:5]
        closest_V3 = cal_V3.iloc[(cal_V3['f [MHz]'] - self.fMHz).abs().argsort()][:5]
        # interpolate PdB = a*Vdc + b        
        V1dc_2_PdB = interp1d(closest_V1['NI-dacq(Vdc)'], closest_V1['Pin.(dBm)'], fill_value="extrapolate")
        V2dc_2_PdB = interp1d(closest_V2['NI-dacq(Vdc)'], closest_V2['Pin.(dBm)'], fill_value="extrapolate")
        V3dc_2_PdB = interp1d(closest_V3['NI-dacq(Vdc)'], closest_V3['Pin.(dBm)'], fill_value="extrapolate")
        
        # probe gain (warning : postitive values)
        cal_ProbeGains = pd.read_csv(self.cal_dir+'SSA84_TaskB_VoltageProbeGains.csv', sep=';')
        ProbeAGain = np.abs(np.interp(self.fMHz, cal_ProbeGains['f [MHz]'], cal_ProbeGains['ProbeA [dB]']))
        ProbeBGain = np.abs(np.interp(self.fMHz, cal_ProbeGains['f [MHz]'], cal_ProbeGains['ProbeB [dB]']))
        ProbeCGain = np.abs(np.interp(self.fMHz, cal_ProbeGains['f [MHz]'], cal_ProbeGains['ProbeC [dB]']))

        ## channel V1 <-> probe A. NB: Cable loss is included in the V1 calibration
        self._df['V1 [dB]'] = V1dc_2_PdB(self._df['V1_raw'])
        # self._df['V1 [dB]'] = 3.2253 * self._df['V1_raw'] - 2.913  # verif @ 61.5 MHz
        self._df['V1 [V]'] = np.sqrt(2*30/1000 * 10**((self._df['V1 [dB]'] + ProbeAGain)/10))

        ## channel V2 <-> probe C. NB: Cable loss is included in the V1 calibration
        self._df['V2 [dB]'] = V2dc_2_PdB(self._df['V2_raw'])
        # self._df['V2 [dB]'] = 3.2208 * self._df['V2_raw'] - 2.7765  # verif @ 61.5 MHz
        self._df['V2 [V]'] = np.sqrt(2*30/1000 * 10**((self._df['V2 [dB]'] + ProbeCGain)/10))

    def raw_Vac_to_Vac(self):
        """
        Process pressure signals.
        
        The results are pressure in Pa.
        """
        # Pfeiffer PKR 361
        def p(U):
            d = 9.333
            return 10**(1.667*U - d)

        self._df['JR3'] = p(self._df['JR3_raw'])
        self._df['JR4'] = p(self._df['JR4_raw'])
        
    def raw_Tc_to_Tc(self):
        """
        Process the thermocouple signals.
        
        The results are in degree C
        """
        cal_Tc = pd.read_csv(self.cal_dir+'SSA84_TaskB_calibration_TC.csv', sep=';')
        Tc1_to_T = interp1d(cal_Tc['TC1 (Vdc)'], cal_Tc['Tin (degC)'], fill_value="extrapolate")
        Tc2_to_T = interp1d(cal_Tc['TC2 (Vdc)'], cal_Tc['Tin (degC)'], fill_value="extrapolate")
        Tc3_to_T = interp1d(cal_Tc['TC3 (Vdc)'], cal_Tc['Tin (degC)'], fill_value="extrapolate")
        Tc4_to_T = interp1d(cal_Tc['TC4 (Vdc)'], cal_Tc['Tin (degC)'], fill_value="extrapolate")
        
        self._df['TC1'] = Tc1_to_T(self._df['TC1_raw'])
        self._df['TC2'] = Tc2_to_T(self._df['TC2_raw'])
        self._df['TC3'] = Tc3_to_T(self._df['TC3_raw'])
        self._df['TC4'] = Tc4_to_T(self._df['TC4_raw'])        
        
        # Smooth temperature
        self._df['TC1_smooth'] = self._df['TC1'].ewm(span = 100).mean()
        self._df['TC2_smooth'] = self._df['TC2'].ewm(span = 100).mean()
        self._df['TC3_smooth'] = self._df['TC3'].ewm(span = 100).mean()
        self._df['TC4_smooth'] = self._df['TC4'].ewm(span = 100).mean()        
        
    def Vprobe_to_Vmax_and_Imax(self):
        """
        Deduce the max voltage and currents from the measured voltages.
        
        The voltage probes are located:
            - from the T-middle for probe A (Tuning side)
                241 + (165+395)/2*(pi/2) + 552.5 ~ 1233 mm. 
                HFSS gives 1239 mm
              --> 1236 mm +/- 3 mm
                
            - from the T-middle for probe C (DUT side)
                175 + 485 mm = 660 mm (theoretical from CAD)
                (from measured)
              --> 660 mm +/- TBD
                We can use the same uncertainty
        
        """
        # VprobeCEA -> V max CEA: 1.000399052468527
        # VprobeDUT -> V max DUT: 1.194556380161787
        # VprobeCEA -> I short CEA: 0.03372662249801389
        # VprobeDUT -> I short DUT: 0.06329607347946643
      

        # VprobeCEA -> V max CEA: 1.000560031267852
        # VprobeDUT -> V max DUT: 1.2012721011809484
        # VprobeCEA -> I short CEA: 0.03374709546042175
        # VprobeDUT -> I short DUT: 0.06368098648604123

        self._df['V_CEA_max'] = 1.0006 * self._df['V1 [V]']
        self._df['V_DUT_max'] = 1.2013 * self._df['V2 [V]']
        
        self._df['I_CEA_max'] = 0.0338 * self._df['V1 [V]']
        self._df['I_DUT_max'] = 0.0637 * self._df['V2 [V]']
        
        
    def to_hdf(self, filename):
        """
        Export the data into a HDF file

        Parameters
        ----------
        filename : string
            hdf filename.

        """
        # reduce the size of the float to make lighter file
        _df = self.df.copy()
        for col in _df.columns:
            if _df[col].dtype == 'float64':
                 _df[col] = _df[col].astype('float32')
        # export to HDF
        _df.to_hdf(filename, 'SSA84')
        
        