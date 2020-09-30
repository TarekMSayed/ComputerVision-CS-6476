#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from skimage.util import random_noise

# read image
img = cv2.imread("images/moon.png", 0)
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# add noise to the image
# the output image of random_noise function is float64 which is not supported by opencv
noisy_image = random_noise(img, 's&p', amount=0.02).astype('float32')
cv2.imshow("noisy image", noisy_image)
kernel_size = 3  # try 5
median_filtered = cv2.medianBlur(noisy_image, kernel_size)
cv2.imshow("median_filtered", median_filtered)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
