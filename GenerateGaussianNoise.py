#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:53:32 2019

@author: Tarek M. Sayed
Email: atamish@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt

noise = np.random.randn(20,1)
x = np.linspace(-3,3,10)
plt.hist(noise, x)
