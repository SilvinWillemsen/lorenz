#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This file is called from each individual case<number>.py file and generates the data and plots for each case.

The data 
"""
import sys
sys.path.append('../')

import os
import h5py
from lorenz.solver import solve
import pandas as pd
from lorenz.plotting import plotLorenz



def case_generation(initial_conditions, case_number, action, file_name, dt, N):
    """
    

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
        
        print('Simulation started...')
        x0 = initial_conditions[0]
        y0 = initial_conditions[1]
        z0 = initial_conditions[2]
        
        simulation_result = solve(x0, y0, z0, scheme_variables.loc[case_number-1, 'sigma'],
                                              scheme_variables.loc[case_number-1, 'beta'],
                                              scheme_variables.loc[case_number-1, 'rho'], dt, N)
        print('Simulation finished!')
        
        # save data
        print ('Saving data...')
        f = h5py.File('output_files/' + file_name + '_output/simulation_result.hdf5', 'w')
        f.create_dataset('xyzData', data = simulation_result)
        f.create_dataset('dt', data = dt)
        f.close()
        print ('Data saved!')
        
    elif action == 'load':
        # Once the simulation has and the data has been saved, the data can be 
        # loaded instead of simulated again.
        print ('Loading data...')
        
        try:
            f = h5py.File('output_files/' + file_name + '_output/simulation_result.hdf5', 'r')
        except OSError:
            raise Exception("Data has not been generated yet! change the 'action' variable to 'simulate'.")
            sys.exit()
            
        simulation_result = f['xyzData'][...]
        dt = f['dt'][...]

        f.close()
        print ('Data loaded!')
    
    
    # plot and save plots to pdf
    print ('Generating plots...')
    plotLorenz(simulation_result, dt, file_name)
    print ('Done generating plots!')