#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cv2
# read image
img = cv2.imread("images/dolphin.png", 0)
print('Image Dimension    : ', img.shape)
print('Image Height       : ', img.shape[0])
print('Image Width        : ', img.shape[1])
# print('Number of Channels : ', img.shape[2])
print('Object type        : ', type(img))
print('Elements data type : ', img.dtype)
print(img)
print(img[100, 200])
plt.plot(img)
plt.show()
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
cv2.imshow("image_1", img)
# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
