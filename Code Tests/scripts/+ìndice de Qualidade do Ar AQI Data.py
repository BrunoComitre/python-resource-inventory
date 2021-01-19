# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 16:48:23 2018

@author: bruno
"""

import numpy as np

# air quality index AQI data
hong_kong = np.array (
    [42, 40, 41, 43, 44, 43 ])
new_york = np.array (
    [30, 31, 29, 29, 29, 30 ])
montreal = np.array (
    [ 11, 11, 12, 13, 11, 12 ])
     
     
hk_mean = (hong_kong [0] +
           hong_kong [-1]) / 2.0

ny_mean = (new_york [1] +
           new_york [-3]) / 2.0
           
m_mean = (montreal [1] +
          montreal [-0]) / 2.0

print (hk_mean)
print (ny_mean)
print (m_mean)
