#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This file generates the data and plots for case 2

Once the data has been generated and saved to disk the 'action' variable can
be changed from 'simulate' to 'load', to load the data from disk instead.

"""

import os
from cases_generator import case_generation


# action can be 'simulate' or 'load'
action = 'simulate'
case = 2
initial_conditions = (1.0, 1.0, 1.0)

# retrieve file name for correct folder structure later on
file_name = os.path.basename(__file__).replace(".py", "")

# call case_generation function
case_generation (initial_conditions, case, action, file_name)