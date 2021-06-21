#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:44:05 2021

@author: SilvinW

"""
import matplotlib.pyplot as plt
import numpy as np
import time


def _plot2D (vecs, vel_vecs, num_hor, num_vert, idx_to_plot, scatter_size):
    
    """
    Internal function to be used from plotting.plotLorenz(...). The function 
    generates a 2D plot from two columns of the data in vecs determined by
    num_hor (x-axis) and num_vert (y-axis). Variables are called [hor]izontal 
    and [vert]ical as to not confuse with the spatial coordinates x and y.


    INPUT::  
        
        vecs : tuple (3) of (Numpy) Arrays of floats
            The (x, y, z)-coordinate over time ((x, y, z)[n]). Columns contain
            x,y and z respectively.
        
        vel_vecs : tuple (3) of (Numpy) Arrays of floats
            The velocities of x, y and z respectively.
    
        num_hor : (Numpy) Arrays of floats
            What column of vecs and vel_vecs to use for the horizontal (x) axis.
        
        num_vert : (Numpy) Arrays of floats
            What column of vecs and vel_vecs to use for the vertical (y) axis.

        idx_to_plot : range
            Range object containing the temporal indices to plot.
        
        scatter_size : int
            Size of the plotted points.

    OUTPUT::
        
        None.

    """
    
    # initialise figure
    fig = plt.figure(figsize=(7, 5))
    fig.add_axes([0.05, 0.1, 0.8, 0.8])
    axis_names = ['x', 'y', 'z']
    vel_vec = np.sqrt(vel_vecs[num_hor]**2 + vel_vecs[num_vert]**2);
    
    # plot state of the system with colours denoting velocity
    p = plt.scatter (vecs[num_hor][idx_to_plot], 
                     vecs[num_vert][idx_to_plot],
                     s = scatter_size,
                     c = vel_vec[idx_to_plot])
    
    # plot initial condition (in red)
    plt.scatter (vecs[num_hor][0], vecs[num_vert][0], s = scatter_size*2, c = 'red')
       
    # add axis labels
    plt.xlabel (axis_names[num_hor])
    plt.ylabel (axis_names[num_vert])
    
    plt.title('2D plot of (' + axis_names[num_hor] + ',' + axis_names[num_vert] + ') view')

    # add grid
    plt.grid (True)
    
    # add colourbar
    cbaxes = fig.add_axes([0.88, 0.1, 0.03, 0.8]) 
    cb = plt.colorbar(p, cax = cbaxes)  
    cbaxes.set_ylabel('velocity', rotation=0, position=(1,1.05))
    
    
    
def plotLorenz (vecs, dt, file_name = "", step_size = 5, scatter_size = 10):
    
    """
    
    Function that plots the result of the ODE simulation lorenz.solver.solve(...)
    and saves plots to .pdf files if file_name != "".
    
    The plots use the matplotlib.pyplot functionality and the scatter function
    and colourcode the plots based on the velocity of the system. 

    The initial condition of the ODE simulation :math:`(x_0, y_0, z_0)` --  is 
    plotted in red, whereas the rest of the colours are determined by the
    velocity data stored in vel_vecs.
    

    Two plots are generated:
        A subplot containing the following three perspectives
        :math:`(x,y)`
        :math:`(x,z)`
        :math:`(y,z)`
    
        A 3D plot with all axes :math:`(x, y, z)`
        
    INPUT::
    
        vecs : tuple of (Numpy) Arrays of floats
            The (x, y, z)-coordinate over time ((x, y, z)[n]).
            
        dt : float
            Time step (s).
            
        file_name : string, optional
            Name of the file calling this function. Needed for storing files
            in the correct folder. The default is "" and no files will be
            saved if file_name = "".
            
        step_size : int, optional
            Determines the (discrete) temporal interval between two plotted points.
            The default is 5.
            
        scatter_size : int, optional
            Size of the points in the scatterplot. The default is 10.

    OUTPUT:: 
        
        None.


    """

    
    if file_name == "":
        save_files = False
        print ('Generating plots...')

    else:
        save_files = True
        print ('Generating plots and saving files...')

        
    tic = time.time();
    
    # Initialise velocity vectors for colouring the plots
    N = vecs[0].shape[0]
    x_vel = np.zeros(N)
    y_vel = np.zeros(N)
    z_vel = np.zeros(N)

    dt = 0.002 # DONT FORGET TO CHANGE

    x_vel = (vecs[0][1:] - vecs[0][0:-1]) / dt
    y_vel = (vecs[1][1:] - vecs[1][0:-1]) / dt
    z_vel = (vecs[2][1:] - vecs[2][0:-1]) / dt

    vel_vecs = (x_vel, y_vel, z_vel)

    # calculate 3D velocity vector
    xyz_vel = np.sqrt (vel_vecs[0]**2 + vel_vecs[1]**2 + vel_vecs[2]**2)

    
    # PLOTTING 2D #
    
    idx_to_plot = range (step_size, N-1, step_size);
    
    # Generate 2D plots using plot2D function
    _plot2D (vecs, vel_vecs, 0, 1, idx_to_plot, scatter_size)
    if save_files:
        plt.savefig('output_files/' + file_name + '_output/xyPlot.pdf')
        
    _plot2D (vecs, vel_vecs, 0, 2, idx_to_plot, scatter_size)
    if save_files:
        plt.savefig('output_files/' + file_name + '_output/xzPlot.pdf')
        
    _plot2D (vecs, vel_vecs, 1, 2, idx_to_plot, scatter_size)
    if save_files:
        plt.savefig('output_files/' + file_name + '_output/yzPlot.pdf')


    # PLOTTING 3D #

    fig = plt.figure()
    ax = plt.subplot (projection='3d', position=[0.05, 0.1, 0.8, 0.8])
    ax.scatter (vecs[0][0],
                vecs[1][0],
                vecs[2][0],
                s = scatter_size*2,
                c = 'red')

    p = ax.scatter (vecs[0][idx_to_plot],
                vecs[1][idx_to_plot],
                vecs[2][idx_to_plot],
                s = scatter_size,
                c = xyz_vel[idx_to_plot])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D plot')

    cbaxes = fig.add_axes([0.85, 0.1, 0.03, 0.8]) 
    cb = plt.colorbar(p, cax = cbaxes)  
    cbaxes.set_ylabel('velocity', rotation=0, position=(0, 0.99))
    
    if save_files:
        plt.savefig('output_files/' + file_name + '_output/xyzPlot.pdf')

    toc = time.time() - tic
    if save_files:
        print (f'Done generating plots and saving files! It took {toc:1.3} seconds to generate the plots and save the files.')

    else:
        print (f'Done generating plots! It took {toc:1.3} seconds to generate the plots.')
