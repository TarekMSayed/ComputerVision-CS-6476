#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 06:40:51 2019

@author: Tarek M. Sayed
Email: atamish@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("images/fruit.png", 1)
sigma = 64
for sigma in range(2,80, 2**4):
    noise = np.random.randn(*img.shape) * sigma
    cv2.imshow("sigma = " + str(sigma), noise)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()