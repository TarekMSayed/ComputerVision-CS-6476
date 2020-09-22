#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cv2
# read image
img = cv2.imread("images/fruit.png", 1)
print('Image Dimension    : ', img.shape)
print('Image Height       : ', img.shape[0])
print('Image Width        : ', img.shape[1])
print('Number of Channels : ', img.shape[2])
print('Object type        : ', type(img))
print('Elements data type : ', img.dtype)
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
cv2.imshow("image_1", img)
cv2.imshow("red", red)
cv2.imshow("green", green)
cv2.imshow("blue", blue)
# cv2.imshow("crop_image", crop)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
