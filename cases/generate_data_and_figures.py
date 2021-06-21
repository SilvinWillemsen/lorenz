#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This file is called from each individual case<number>.py file and generates the data and plots for each case.

The data can be simulated or loaded from disk. 

"""
import sys
sys.path.append('../')

import os
import h5py
import pandas as pd
import time

from lorenz.solver import solve
from lorenz.plotting import plotLorenz



def generate_data_and_figures(initial_conditions, case_number, action, file_name, dt, N):
    """

    Function that generates the data and figures for a certain case.

    INPUT:: 
        
        initial_conditions : tuple
            Contains the initial conditions for the system (x0, y0, z0)
        case_number : int
            The case number (1-5).
        action : string
            Action can be 'simulate' or 'load' to either simulate the data or load 
            from the disk instead.
        file_name : string
            Name of the file that called this function.
        dt : float
            Time step (s).
        N : int
            Number of iterations.
            
    OUTPUT:: 
        
        None.

    """
    
    if case_number < 1 | case_number > 5:
        raise Exception ("Case number should be in the range 1 to 5 (included)")
    
    if action == 'simulate':
    
        scheme_variables = pd.read_csv('scheme_variables.csv')        
        
        x0 = initial_conditions[0]
        y0 = initial_conditions[1]
        z0 = initial_conditions[2]
        
        simulation_result = solve(x0, y0, z0, scheme_variables.loc[case_number-1, 'sigma'],
                                              scheme_variables.loc[case_number-1, 'beta'],
                                              scheme_variables.loc[case_number-1, 'rho'], dt, N)
    
        
        # save data
        print ('Saving data...')
        tic = time.time();
        
        f = h5py.File('output_files/' + file_name + '_output/simulation_result.hdf5', 'w')
        f.create_dataset('xyzData', data = simulation_result)
        f.create_dataset('dt', data = dt)
        f.close()
        
        toc = time.time() - tic
        print (f'Data saved! It took {toc:1.3} seconds to save the data.')
        
    elif action == 'load':
        # Once the simulation has and the data has been saved, the data can be 
        # loaded instead of simulated again.
        print ('Loading data...')
        tic = time.time();

        try:
            f = h5py.File('output_files/' + file_name + '_output/simulation_result.hdf5', 'r')
        except OSError:
            raise Exception("Data has not been generated yet! change the 'action' variable to 'simulate'.")
            sys.exit()
            
        simulation_result = f['xyzData'][...]
        dt = f['dt'][...]

        f.close()
        
        toc = time.time() - tic
        print (f'Data loaded! It took {toc:1.3} seconds to load the data.')
    
    
    # plot and save plots to pdf
    plotLorenz(simulation_result, dt, file_name)