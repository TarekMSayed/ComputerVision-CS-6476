#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread("images/tablet.png", 0)
template = img[75:165, 150:185].copy()
width, height = template.shape[::-1]
# cv2.imshow("image", img)
# cv2.imshow("Template", template)
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# print(result)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(img, top_left, bottom_right, 255, 2)

plt.subplot(121), plt.imshow(result, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
