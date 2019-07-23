# -*- coding: utf-8 -*-
import cv2
import numpy as np


def match_template(img_src, img_template, threshold=0.9):
    img_template_width, img_template_height, _ = img_template.shape

    res = cv2.matchTemplate(img_src, img_template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, _ = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # change threshold in order to return only the different instances
        threshold = max_val - 0.01

        loc = np.where(res >= threshold)

        return list(zip(*loc[::-1]))
    else:
        return []
