
import lorenz.finiteDifferences as FD
import numpy as np
import time


def solve (x, y, z, sigma, beta, rho, dt = 0.002, N = 5000):
    """

    This function solves the Lorenz Attractor ODE system using Euler's method.

    INPUT::
        
        x : float
        Initial condition of the x-coordinate (m).
        
        y : float
        Initial condition of the y-coordinate (m).
        
        z : float
        Initial condition of the z-coordinate (m).
        
        sigma : float
        Prandtl number (m^2/s).
        
        beta : float
        Free parameter.
        
        rho : float
        Free parameter.
        
        dt : float, optional
        Time step (s). The default is 0.002.
        
        N : int, optional
        Number of iterations. The default is 5000.

    OUTPUT::
    
        Tuple of the following arrays:
                
            xVec : (Numpy) Array of floats
            The x-coordinate over time (x[n]).
            
            yVec : (Numpy) Array of floats
            The y-coordinate over time (y[n]).
            
            zVec : (Numpy) Array of floats
            The z-coordinate over time (z[n]).
         
            
    """
    
    # initialise temporal vectors
    xVec = np.zeros(N);
    yVec = np.zeros(N);
    zVec = np.zeros(N);

    print('Simulation started...')
    tic = time.time();

    # main loop
    for i in range(N):
        x, y, z = FD.update_system_state (x, y, z, sigma, beta, rho, dt)
        xVec[i] = x
        yVec[i] = y
        zVec[i] = z
        
    toc = time.time() - tic
    print(f'Simulation finished! It took {toc:1.3} seconds to simulate.')
        
    #return the temporal vectors
    return (xVec, yVec, zVec)
        