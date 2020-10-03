#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2


def find_template(s, t):
    # TemplateMatchModes
    # https://docs.opencv.org/3.4/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d
    result = cv2.matchTemplate(s, t, cv2.TM_CCOEFF_NORMED)
    print(result)
    found_pattern_start = np.argmax(result)
    found_pattern = s[found_pattern_start:found_pattern_start + len(t)]
    print("pattern started at: ", found_pattern_start)
    print("found pattern: ", found_pattern)
    print("Template     : ", t)


source = np.array([-1, 0, 0, 1, 1, 1, 0, -1, -1, 0, 1, 0, 0, -1], dtype=np.float32)

template_1 = np.array([1, 1, 0], dtype=np.float32)
print("Template Ex 1")
find_template(source, template_1)


template_2 = np.array([0, -1, -1, 0], dtype=np.float32)
print("Template Ex 2")
find_template(source, template_2)

partial_matched_template = np.array([1, 1, 1, 0, 0], dtype=np.float32)
print("Partial Matched Template Ex")
find_template(source, partial_matched_template)
