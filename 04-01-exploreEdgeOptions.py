#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2

# read image
img = cv2.imread("images/fall-leaves.png", 1)
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# create gaussian filter
filter_size = 21
filter_sigma = 3
# borderType options
"""
BORDER_CONSTANT    = 0,
BORDER_REPLICATE   = 1,
BORDER_REFLECT     = 2,
BORDER_WRAP        = 3, # In Documentation not supported in GaussianBlur() but works
BORDER_REFLECT_101 = 4,
BORDER_TRANSPARENT = 5,
BORDER_REFLECT101  = BORDER_REFLECT_101,
BORDER_DEFAULT     = BORDER_REFLECT_101,
BORDER_ISOLATED    = 16
"""

wrap = cv2.GaussianBlur(img, (filter_size, filter_size), filter_sigma, sigmaY=filter_sigma
                           , borderType=3)
cv2.imshow("wrap/circular image", wrap)

reflect = cv2.GaussianBlur(img, (filter_size, filter_size), filter_sigma, sigmaY=filter_sigma
                           , borderType=2)
cv2.imshow("reflect/symmetric image", reflect)

replicate = cv2.GaussianBlur(img, (filter_size, filter_size), filter_sigma, sigmaY=filter_sigma
                             , borderType=1)
cv2.imshow("replicate/copy edge image", replicate)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
