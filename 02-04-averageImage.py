#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cv2
# read image
dolphin_img = cv2.imread("images/dolphin.png", 0)
bicycle_img = cv2.imread("images/bicycle.png", 0)
sum_img = dolphin_img + bicycle_img
average = (dolphin_img//2) + (bicycle_img//2)
wrong_average = sum_img // 2
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
cv2.imshow("dolphin", dolphin_img)
cv2.imshow("bicycle", bicycle_img)
cv2.imshow("sum", sum_img)
cv2.imshow("average", average)
cv2.imshow("wrong_average", wrong_average)

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
