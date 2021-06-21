"""
Created on Wed Jun 16 13:33:34 2021

@author: SilvinW



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
dt = 0.005

# number of iterations
N = 10000



# choose case
case = 0


# create dataframe with values for sigma, beta and rho for 5 cases
casesData = [[10.0, 8/3, 6.0],
             [10.0, 8/3, 16.0],
             [10.0, 8/3, 28.0],
             [14, 8/3, 28],
             [14, 13/3, 28]]

casesDataFrame = pd.DataFrame (casesData, columns=['sigma', 'beta', 'rho'])


xVec, yVec, zVec = solver.solve (x0, y0, z0, 
                            casesDataFrame.loc[case, 'sigma'],
                            casesDataFrame.loc[case, 'beta'],
                            casesDataFrame.loc[case, 'rho'])

plotting.plotLorenz ((xVec, yVec, zVec))

