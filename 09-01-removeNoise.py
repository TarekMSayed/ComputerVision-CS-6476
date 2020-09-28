#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2


def fspecial_gaussian(std: int, kernel_size: int):
    """
    generate a (2k+1)x(2k+1) gaussian kernel with mean=0 and sigma(std deviation) = s
    author: Sandipan Dey
    source: https://stackoverflow.com/questions/17190649/how-to-obtain-a-gaussian-filter-in-python
    :param std: Gaussian sigma (standard deviation)
    :param kernel_size: Kernel size
    :return: numpy array with size (2k+1)x(2k+1)
    """
    s, k = std, kernel_size
    probs = [np.exp(-z * z / (2 * s * s)) / np.sqrt(2 * np.pi * s * s) for z in range(-k, k + 1)]
    # print(probs)
    kernel = np.outer(probs, probs)
    # print(kernel)
    return kernel


# read image
img = cv2.imread("images/saturn.png", 0)
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# add noise
noise = np.random.randn(*img.shape)
sigma_noise = 25
noisy_img = (img + noise * sigma_noise).astype("uint8")
# cv2.imshow("image", img)
cv2.imshow("noisy image", noisy_img)

# create gaussian filter
filter_size = 11
filter_sigma = 2
filter = fspecial_gaussian(filter_sigma, filter_size)

# apply filter to remove noise
smoothed = cv2.filter2D(noisy_img, -1, filter)
cv2.imshow("smoothed image", smoothed)
# using opencv replace fspecial_gaussian and imfilter in MAtLab with one function
blurred = cv2.GaussianBlur(noisy_img, (filter_size, filter_size), filter_sigma)
cv2.imshow("blurred image", blurred)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
