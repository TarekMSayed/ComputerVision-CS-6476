#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
# read image
img = cv2.imread("images/saturn.png", 0)
noise = np.random.randn(*img.shape)
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
sigma_values = (1, 2, 32, 64)
cv2.imshow("image", img)
for sigma in sigma_values:
    cv2.imshow("image with noise with sigma= " + str(sigma), (img + noise*sigma).astype("uint8"))

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
