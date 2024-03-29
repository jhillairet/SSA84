# -*- coding: utf-8 -*-
"""
T-resonator data analysis convenience classes and functions.

J.Hillairet, 2022
"""
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
    def __init__(self, filename:str, contact_type='staubli'):
        '''
        T-Resonator data 

        Parameters
        ----------
        filename : str
            path to a .tdms or a .hdf file
        contact_type : str
            'staubli' (default) or 'arkadia'

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
                self.Vprobe_to_Vmax_and_Imax(contact_type=contact_type)
                self.raw_P_to_P()
                self.raw_Vac_to_Vac()
                self.raw_Tc_to_Tc()
                # VSWR
                self._df['SWR'] = (1 + np.sqrt(self._df['Pr_mean']/self._df['Pi_mean']))/(1 - np.sqrt(self._df['Pr_mean']/self._df['Pi_mean']))
                

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
        
    def Vprobe_to_Vmax_and_Imax(self, contact_type='staubli'):
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
        if contact_type == 'staubli':
            # VprobeCEA -> V max CEA: 1.000560031267852
            # VprobeDUT -> V max DUT: 1.2012721011809484
            # VprobeCEA -> I short CEA: 0.03374709546042175
            # VprobeDUT -> I short DUT: 0.06368098648604123
    
            self._df['V_CEA_max'] = 1.0006 * self._df['V1 [V]']
            self._df['V_DUT_max'] = 1.2013 * self._df['V2 [V]']
            
            self._df['I_CEA_max'] = 0.0338 * self._df['V1 [V]']
            self._df['I_DUT_max'] = 0.0637 * self._df['V2 [V]']

        elif contact_type == 'arkadia':
            # VprobeCEA -> V max CEA: 1.0031203682262384
            # VprobeDUT -> V max DUT: 1.2842791840489434
            # VprobeCEA -> I short CEA: 0.0337109785482888
            # VprobeDUT -> I short DUT: 0.06829468196254714

            self._df['V_CEA_max'] = 1.0031 * self._df['V1 [V]']
            self._df['V_DUT_max'] = 1.2843 * self._df['V2 [V]']
            
            self._df['I_CEA_max'] = 0.0337 * self._df['V1 [V]']
            self._df['I_DUT_max'] = 0.0683 * self._df['V2 [V]']
            
        
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
        
    def plot(self, backend='matplotlib'):
        """
        Plot the data.

        Parameters
        ----------
        backend : str, optional
            Backend to plot the data with: 'matplotlib', 'hvplot' or 'pyqtgraph'.
            The default is 'matplotlib'.

        """
        if backend == 'matplotlib':
            _df = self.df
            
            fig, ax = plt.subplots(5, 1, sharex=True)
            _df.plot(y='Pi [W]', ax=ax[0])
            _df.plot(y='Pr [W]', ax=ax[0])

            _df.plot(y='V1 [V]', ax=ax[1])
            _df.plot(y='V2 [V]', ax=ax[1])

            _df.plot(y='I_CEA_max', ax=ax[2])
            _df.plot(y='I_DUT_max', ax=ax[2])

            _df.plot(y='JR3', ax=ax[3])
            _df.plot(y='JR4', ax=ax[3])

            ax[3].set_yscale('log')

            _df.plot(y='TC1', ax=ax[4])
            _df.plot(y='TC2', ax=ax[4])
            _df.plot(y='TC3', ax=ax[4])
            _df.plot(y='TC4', ax=ax[4])

            ax[0].set_title(f'SSA84 - {self.date} - {self.time} - f={self.fMHz} MHz')
            fig.autofmt_xdate(rotation=45)
            return fig, ax
        elif backend == 'pyqtgraph':
            try:
                import pyqtgraph as pg
                import matplotlib.dates as mdates
            except ImportError as e:
                print(e)
            pg.setConfigOption('background', 'w')
            pg.setConfigOption('foreground', 'k')
            pg.setConfigOptions(antialias=True)  # prettier plots

            win = pg.GraphicsLayoutWidget()
            # win.ci.layout.setContentsMargins(0, 0, 0, 0)
            
            time = mdates.date2num(self.df.index)
            p_power = win.addPlot(row=0, col=0)
            p_power.plot(time, self.df['Pi [W]'], pen='b', name='Pi')
            p_power.plot(time, self.df['Pr [W]'], pen='r', name='Pr')
            p_power.setLabels(left='Power [W]')
            # p_power.hideAxis("bottom")

            p_voltage = win.addPlot(row=1, col=0)
            p_voltage.plot(time, self.df['V1 [V]'], pen='b', name='V1')
            p_voltage.plot(time, self.df['V2 [V]'], pen='r', name='V2')
            p_voltage.setLabels(left='Voltage [V]')
            
            p_current = win.addPlot(row=2, col=0)
            p_current.plot(time, self.df['I_CEA_max'], pen='b', name='I_CEA')
            p_current.plot(time, self.df['I_DUT_max'], pen='r', name='I_DUT')
            p_current.setLabels(left='Current [A]')

            p_pressure = win.addPlot(row=3, col=0)
            p_pressure.plot(time, self.df['JR3'], pen='b', name='JR3')
            p_pressure.plot(time, self.df['JR4'], pen='r', name='JR4')            
            p_pressure.setLogMode(False, True)
            p_pressure.setLabels(left='Pressure [Pa]')

            p_temp = win.addPlot(row=4, col=0)
            p_temp.plot(time, self.df['TC1'], pen='b', name='TC1')
            p_temp.plot(time, self.df['TC2'], pen='r', name='TC2')
            p_temp.plot(time, self.df['TC3'], pen='c', name='TC3')
            p_temp.plot(time, self.df['TC4'], pen='m', name='TC4')
            p_temp.setLabels(left='Temperature [°C]', bottom='time')
            
            ps = (p_power, p_voltage, p_current, p_pressure, p_temp)            
            
            # grid
            for p in ps:
                p.showGrid(x = True, y = True, alpha = 0.3)
            # synchronize x-scales
            for p in ps[1:]:
                p.setXLink(p_power)
            
            win.showMaximized()
            win.setWindowTitle(f'SSA84 - {self.date} - {self.time} - f={self.fMHz} MHz')
            win.show()

            return win, ps

def find_shots_indices(array, threshold):
    """
    Returns the start and stop arrays indices corresponding to RF shot.

    Parameters
    ----------
    array : numpy array
        Array to threshold on
    threshold : float
        threshold to appy

    Returns
    -------
    idx_starts : list of int
    idx_stops : list of int
    """
    # indices of values above threshold
    idx_thres = np.nonzero(array > threshold)[0]
    if idx_thres.size > 0:  # not empty
        # find indices where we change the RF shot   
        idx_starts = np.append(idx_thres[0], idx_thres[1:][np.diff(idx_thres) > 1])
        
        idx_stops = np.append(idx_thres[0:-1][np.diff(idx_thres) > 1], idx_thres[-1])
 
        return idx_starts, idx_stops
    else:
        return None, None

def split_array(array, idx_starts, idx_stops):
    """
    Split an numerical array into sub-arrays according to start and stop indices.

    Parameters
    ----------
    array : numpy array
    idx_starts : list of int
    idx_stops : list of int

    Returns
    -------
    arrays : list of array
    """
    arrays = []    
    for idx_start, idx_stop in zip(idx_starts, idx_stops):
        arrays.append(array[idx_start:idx_stop])
    return arrays

def stats(subarray_list):
    """
    Extract the (mean, std, min, max) values of each subarrays

    Parameters
    ----------
    subarray_list : list of numpy array

    Returns
    -------
    stats : list of array

    """
    stats = []
    for arr in subarray_list:
        if arr.size > 0: # not empty
            stats.append([np.mean(arr), np.std(arr), np.min(arr), np.max(arr)])

    return stats

def create_resumed_parameters(hdf_files):
    """
    Return the resumed parameters (mean, std, min, max) of resonator data.

    Parameters
    ----------
    hdf_files : list
        list of HDF files

    Returns
    -------
    db : pd.DataFrame
        resumed data.

    """
    V1_stats = []
    V2_stats = []
    I_CEA_stats = []
    I_DUT_stats = []
    Pi_stats = []
    Pr_stats = []
    JR3_stats = []
    JR4_stats = []
    time_stats = []
    pulse_lengths = []
    
    for hdf_file in tqdm(hdf_files):
        data = TResonatorData(hdf_file)
        # find start and stop times of each RF pulses
        # smoothing data a bit to avoid counting breakdown as the stop of the pulse
        idx_starts, idx_stops = find_shots_indices(data.df['V1 [V]'].ewm(span = 200).mean().values, 50)
    
        if idx_starts is not None:
            times = split_array(data.df['time_absolute'].values, idx_starts, idx_stops)
            subV1s = split_array(data.df['V1 [V]'].values, idx_starts, idx_stops)
            subV2s = split_array(data.df['V2 [V]'].values, idx_starts, idx_stops)
            subI_CEAs = split_array(data.df['I_CEA_max'].values, idx_starts, idx_stops)
            subI_DUTs = split_array(data.df['I_DUT_max'].values, idx_starts, idx_stops)          
            subPis = split_array(data.df['Pi [W]'].values, idx_starts, idx_stops)
            subPrs = split_array(data.df['Pr [W]'].values, idx_starts, idx_stops)
            subJR3s = split_array(data.df['JR3'].values, idx_starts, idx_stops)
            subJR4s = split_array(data.df['JR4'].values, idx_starts, idx_stops)        
            
            # calculate the pulse duration in seconds
            durations = []
            for idx, time in enumerate(idx_starts):
                durations.append((data.df['time_absolute'][idx_stops][idx] - data.df['time_absolute'][idx_starts][idx]).total_seconds())
            pulse_lengths.append(durations)

            time_stats.append([t.flatten()[0] for t in times if t.size > 0])
            V1_stats.append(stats(subV1s))
            V2_stats.append(stats(subV2s))
            I_CEA_stats.append(stats(subI_CEAs))
            I_DUT_stats.append(stats(subI_DUTs))
            Pi_stats.append(stats(subPis))
            Pr_stats.append(stats(subPrs))
            JR3_stats.append(stats(subJR3s))
            JR4_stats.append(stats(subJR4s))
    
    times_mmm = np.hstack(np.array(time_stats, dtype=object))
    V1_mmm = np.vstack(np.array(V1_stats, dtype=object))
    V2_mmm = np.vstack(np.array(V2_stats, dtype=object))
    I_CEA_mmm = np.vstack(np.array(I_CEA_stats, dtype=object))
    I_DUT_mmm = np.vstack(np.array(I_DUT_stats, dtype=object))    
    Pi_mmm = np.vstack(np.array(Pi_stats, dtype=object))
    Pr_mmm = np.vstack(np.array(Pr_stats, dtype=object))
    JR3_mmm = np.vstack(np.array(JR3_stats, dtype=object))
    JR4_mmm = np.vstack(np.array(JR4_stats, dtype=object))
    pulse_lengths_mmm = np.hstack(np.array(pulse_lengths, dtype=object))
    # remove zero lengths pulse
    pulse_lengths_mmm = pulse_lengths_mmm[pulse_lengths_mmm != 0]
    
    db = pd.DataFrame(data={
        'V1_mean': V1_mmm[:,0], 'V1_std': V1_mmm[:,1], 'V1_min': V1_mmm[:,2], 'V1_max': V1_mmm[:,3],
        'V2_mean': V2_mmm[:,0], 'V2_std': V2_mmm[:,1], 'V2_min': V2_mmm[:,2], 'V2_max': V2_mmm[:,3],
        'I_CEA_mean': I_CEA_mmm[:,0], 'I_CEA_std': I_CEA_mmm[:,1], 'I_CEA_min': I_CEA_mmm[:,2], 'I_CEA_max': I_CEA_mmm[:,3],
        'I_DUT_mean': I_DUT_mmm[:,0], 'I_DUT_std': I_DUT_mmm[:,1], 'I_DUT_min': I_DUT_mmm[:,2], 'I_DUT_max': I_DUT_mmm[:,3],
        'Pi_mean': Pi_mmm[:,0], 'Pi_std': Pi_mmm[:,1], 'Pi_min': Pi_mmm[:,2], 'Pi_max': Pi_mmm[:,3],
        'Pr_mean': Pr_mmm[:,0], 'Pr_std': Pr_mmm[:,1], 'Pr_min': Pr_mmm[:,2], 'Pr_max': Pr_mmm[:,3],
        'JR3_mean': JR3_mmm[:,0], 'JR3_std': JR3_mmm[:,1], 'JR3_min': JR3_mmm[:,2], 'JR3_max': JR3_mmm[:,3],
        'JR4_mean': JR4_mmm[:,0], 'JR4_std': JR4_mmm[:,1], 'JR4_min': JR4_mmm[:,2], 'JR4_max': JR4_mmm[:,3],
        'pulse_length': pulse_lengths_mmm
        }, index=pd.DatetimeIndex(data=times_mmm, yearfirst=True))
    return db
