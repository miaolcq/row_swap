# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:24:24 2020

@author: dell
"""

import numpy as np
a= np.arange(25).reshape(5,5)
print(a)
a[[0,4],:] = a[[4,0],:] 
print(a)