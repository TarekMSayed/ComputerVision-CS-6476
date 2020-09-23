#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
# read image
dolphin_img = cv2.imread("images/dolphin.png", 0)
bicycle_img = cv2.imread("images/bicycle.png", 0)
diff_img = dolphin_img + bicycle_img
print(np.min(diff_img))
# set window object
# cv2.namedWindow("image_1", cv2.WINDOW_NORMAL)
# show image
# cv2.imshow("dolphin", dolphin_img)
# cv2.imshow("bicycle", bicycle_img)
cv2.imshow("diff", diff_img)

# wait to press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
