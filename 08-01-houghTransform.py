#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:11:36 2019

@author: Tarek M. Sayed
Email: atamish@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# global variables
imagesPath = "images/"
# read image in gray scale
img = cv.imread(imagesPath + "shapes.png")
cv.imshow("orignal image", img)
# convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# extract edges
edges = cv.Canny(gray, 100, 200)
r, r_theta = (1, np.pi/180)
# TODO: sort array according to theta column to get a pretty plot
accum = cv.HoughLines(edges, r, r_theta, threshold=0, min_theta =-np.pi/2, max_theta=np.pi/2).reshape((-1,2))
# check diffirent thresholds 50, 100, 150, 200
peaks = cv.HoughLines(edges, r, r_theta, threshold=150, min_theta =-np.pi/2, max_theta=np.pi/2).reshape((-1,2))
plt.plot(accum[:,1], accum[:,0], linewidth=0.03)
plt.plot(peaks[:,1], peaks[:,0], 'ro')
plt.xlabel('theta')
plt.ylabel('rho')
plt.title('Hough accumulator')
plt.show()
# TODO: review the algorithm and refactor the code
for rho,theta in peaks:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    # plot every line
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# Uncomment the next line to save the output image
#cv.imwrite('houghlines.png',img)
cv.imshow("hough lines", img)
# wait to press any key to close
cv.waitKey(0)
cv.destroyAllWindows()