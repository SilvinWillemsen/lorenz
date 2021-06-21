#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:49:27 2021

@author: SilvinW

Test module for the lorenz attractor file. Two iterations are performed and
the output is compared compared to the expected output using np.allclose as we
are working with floating-point numbers
    

"""


import lorenz.solver as ls
import numpy as np


class TestCalulateLorenzAttractor:
    
    """
    Description of the test functions:
        
    test_zeros:
        x = 0, y = 0, z = 0
        sigma = 0, beta = 0, rho = 0
        
    test_case_one_111:
        x = 1, y = 1, z = 1
        sigma = 10.0, beta = 8/3, rho = 6.0
        
    test_case_one_54m3:
        x = 5, y = 4, z = -3
        sigma = 10.0, beta = 8/3, rho = 6.0
        
    test_case_five_111:
        x = 1, y = 1, z = 1
        sigma = 14.0, beta = 13/3, rho = 28.0
        
    test_case_five_1m4m6:
        x = 1, y = -4, z = -6
        sigma = 14.0, beta = 13/3, rho = 28.0   
            
    """
    
    # All initial conditions and parameters set to 0 should return zeros
    def test_zeros(self):
        assert np.allclose(ls.solve (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 2),
                           (np.array ([0., 0.]), 
                            np.array ([0., 0.]), 
                            np.array ([0., 0.])))
    
    # Case 1 with x = 1, y = 1, z = 1
    def test_case_one_111(self):
        assert np.allclose(ls.solve (1.0, 1.0, 1.0, 10.0, 8/3, 6.0, 0.01, 2),
                           (np.array ([1.   , 1.004]), 
                            np.array ([1.04      , 1.07976667]), 
                            np.array ([0.98333333, 0.96751111])))
        
    # Case 1 with x = 5, y = 4, z = -3
    def test_case_one_54m3(self):
        assert np.allclose(ls.solve (5.0, 4.0, -3.0, 10.0, 8/3, 6.0, 0.01, 2),
                           (np.array ([4.9  , 4.851]),
                            np.array ([4.41   , 4.79318]),
                            np.array ([-2.72      , -2.43137667])))  
                           
    # Case 5 with x = 1, y = 1, z = 1            
    def test_case_five_111(self):
        assert np.allclose(ls.solve (1.0, 1.0, 1.0, 14.0, 13/3, 28.0, 0.01, 2),
                           (np.array([1.    , 1.0364]),
                            np.array([1.26      , 1.51773333]),
                            np.array([0.96666667, 0.93737778])))
        
    # Case 5 with x = 1, y = -4, z = -6            
    def test_case_five_1m4m6(self):
        assert np.allclose(ls.solve (1.0, -4.0, -6.0, 14.0, 13/3, 28.0, 0.01, 2),
                           (np.array([ 0.3   , -0.2488]),
                            np.array([-3.62   , -3.48246]),
                            np.array([-5.78      , -5.54039333])))