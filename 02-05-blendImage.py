#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import cv2

# read image
dolphin_img = cv2.imread("images/dolphin.png", 0)
bicycle_img = cv2.imread("images/bicycle.png", 0)


def blend(first_image_ratio=0.5):
    img = np.uint8(first_image_ratio * dolphin_img) + np.uint8((1 - first_image_ratio) * bicycle_img)
    return img


blend_img = blend(0.75)
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
cv2.imshow("blend_img", blend_img)

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
