"""

This file generates the data and plots for a case. Change the 'case' variable
to a number between 1 and 5 (included). The initial conditions 
:math:`(x[0], y[0], z[0])` can also be changed, as well as the time step 
:math:`t_{\\delta}` and the number of iterations :math:`N`.

The data is generated and saved to a file in a folder that is dependent on the 
case number. Once the data has been generated and saved to disk the 'action'
variable can be changed from 'simulate' to 'load', to load the last-saved data 
from disk instead.

"""

from generate_data_and_figures import generate_data_and_figures


# case number 1-5 
case = 1

# action can be 'simulate' or 'load'
action = 'simulate'


# initial conditions (x0, y0, z0)
initial_conditions = (1.0, 1.0, 1.0)

# time step
dt = 0.002

# number of iterations
N = 10000

# initialise folder name
folder_name = 'case' + str(case)

# call case_generation function
generate_data_and_figures (initial_conditions, case, action, folder_name, dt, N)    