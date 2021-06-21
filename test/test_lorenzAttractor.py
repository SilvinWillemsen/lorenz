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
import pytest


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
        assert np.allclose(ls.solve (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 2),
                           (np.array ([0., 0.]), 
                            np.array ([0., 0.]), 
                            np.array ([0., 0.])))
    
    # Case 1 with x = 1, y = 1, z = 1
    def test_case_one_111(self):
        assert np.allclose(ls.solve (1.0, 1.0, 1.0, 10.0, 8/3, 6.0, 0.002, 2),
                           (np.array([1.     , 1.00016]), 
                            np.array([1.008     , 1.01599067]), 
                            np.array([0.99666667, 0.99336711])))
        
    # Case 1 with x = 5, y = 4, z = -3
    def test_case_one_54m3(self):
        assert np.allclose(ls.solve (5.0, 4.0, -3.0, 10.0, 8/3, 6.0, 0.002, 2),
                           (np.array([4.98   , 4.96204]), 
                            np.array([4.082     , 4.16291824]), 
                            np.array([-2.944     , -2.88764195])))  
                           
    # Case 5 with x = 1, y = 1, z = 1            
    def test_case_five_111(self):
        assert np.allclose(ls.solve (1.0, 1.0, 1.0, 14.0, 13/3, 28.0, 0.002, 2),
                           (np.array([1.      , 1.001456]), 
                            np.array([1.052     , 1.10390933]), 
                            np.array([0.99333333, 0.98682844])))
        
    # Case 5 with x = 1, y = -4, z = -6            
    def test_case_five_1m4m6(self):
        assert np.allclose(ls.solve (1.0, -4.0, -6.0, 14.0, 13/3, 28.0, 0.002, 2),
                           (np.array([0.86    , 0.726048]), 
                            np.array([-3.924     , -3.85774768]), 
                            np.array([-5.956     , -5.91113061])))

    @pytest.mark.parametrize("x0, y0, z0")    
    def test_init_cond(self):
        (x0, y0, z0) = input("Initial conditions: ")
        xVec, yVec, zVec = ls.solve (x0, y0, z0, 14.0, 13/3, 28.0, 0.002, 10000)
        assert np.isnan(xVec[-1]) == False