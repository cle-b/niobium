# -*- coding: utf-8 -*-
import os

import cv2

from niobium.find_image import match_template


img_dir = os.path.dirname(os.path.realpath(__file__))


def test_find_match_template_zero():
    img_src = cv2.imread(os.path.join(img_dir, "html/browsers.png"))
    img_template = cv2.imread(os.path.join(img_dir, "html/browser0.png"))
    res = match_template(img_src, img_template)
    assert len(res) == 0


def test_find_match_template_one():
    img_src = cv2.imread(os.path.join(img_dir, "html/browsers.png"))
    img_template = cv2.imread(os.path.join(img_dir, "html/browser_edge.png"))
    res = match_template(img_src, img_template)
    assert len(res) == 1
    assert (150, 27) == res[0]


def test_find_match_template_three():
    img_src = cv2.imread(os.path.join(img_dir, "html/browsers.png"))
    img_template = cv2.imread(os.path.join(img_dir, "html/browser_firefox.png"))
    res = match_template(img_src, img_template)
    assert len(res) == 3
    assert (321, 21) in res
    assert (478, 153) in res
    assert (27, 157) in res


def test_find_match_template_threshold():
    img_src = cv2.imread(os.path.join(img_dir, "html/browsers.png"))
    img_template = cv2.imread(os.path.join(img_dir, "html/browser_edge_degraded.png"))
    res = match_template(img_src, img_template)
    assert len(res) == 0
    res = match_template(img_src, img_template, 0.8)
    assert len(res) == 1
    assert (150, 27) == res[0]
