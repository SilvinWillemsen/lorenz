"""
Created on Wed Jun 16 13:33:34 2021

@author: SilvinW

From this file you can run the solver and plot the results (without saving the
plots and data).

Variables that can be changed are:
    The initial conditions :math:`x[0]`, :math:`y[0]` and :math:`z[0]`
        - x0
        - y0
        - z0
        
    The time step :math:`t_\\delta`
        - dt
       
    The number of iterations :math:`N`
        - N
    
    The free variables of the ODE system :math:`\\sigma`, :math:`\\beta` and :math:`\\rho`
        - sigma
        - beta
        - rho

"""


import sys
sys.path.append('../')

import pandas as pd
import lorenz.solver as solver
import lorenz.plotting as plotting

    
# initial conditions
x0 = 1.0
y0 = 1.0
z0 = 1.0

# time step
dt = 0.002

# number of iterations
N = 5000

# free variables
sigma = 10.0
beta = 8/3
rho = 6.0

# solve the system
xVec, yVec, zVec = solver.solve (x0, y0, z0, sigma, beta, rho)

# plot the results
plotting.plotLorenz ((xVec, yVec, zVec), dt)