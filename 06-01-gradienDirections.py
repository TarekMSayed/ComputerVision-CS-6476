#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread("images/octagon.png", 0)
# convert image to range [0, 1] for convenience
img = img / 255
# https://docs.opencv.org/master/d5/d0f/tutorial_py_gradients.html
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# Find magnitude and angle
magnitude = np.sqrt(sobelx**2.0 + sobely**2.0)
angle = np.arctan2(sobely, sobelx) * (-180 / np.pi)

plt.subplot(3, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 5), plt.imshow(magnitude, cmap='gray')
plt.title('magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 6), plt.imshow(angle, cmap='gray')
plt.title('angle'), plt.xticks([]), plt.yticks([])
plt.show()
selected = np.where((angle > 30) & (angle < 60) & (magnitude > 1), angle, 0)
cv2.imshow("selected", selected)

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
