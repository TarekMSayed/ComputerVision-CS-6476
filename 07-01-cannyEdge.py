#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# read image
frizzy_img = cv.imread("images/frizzy.png", 0)
froomer_img = cv.imread("images/froomer.png", 0)
frizzy_edges = cv.Canny(frizzy_img, 100, 200)
froomer_edges = cv.Canny(froomer_img, 100, 200)
cv.imshow("frizzy", frizzy_edges)
cv.imshow("froomer", froomer_edges)
# Common pixels
cv.imshow("common", froomer_edges & frizzy_edges)

# wait to press any key to close
cv.waitKey(0)
cv.destroyAllWindows()
