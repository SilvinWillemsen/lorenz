#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    
    File to generate scheme_variables.csv containing the values for variables :math:`sigma`, :math:`beta` and :math:`rho` for all 5 cases

"""

import pandas as pd

# create dataframe with values for sigma, beta and rho for 5 cases
scheme_variables = [[10.0, 8/3, 6.0],
                    [10.0, 8/3, 16.0],
                    [10.0, 8/3, 28.0],
                    [14, 8/3, 28],
                    [14, 13/3, 28]]
variables_data_frame = pd.DataFrame (scheme_variables, columns=['sigma', 'beta', 'rho'])
variables_data_frame.to_csv('scheme_variables.csv')
