# -*- coding: utf-8 -*-
import io

import cv2
import numpy as np
from PIL import Image
from selenium.common.exceptions import NoSuchElementException

from .image_element import ImageElement
from .timeout import ImplicitWait


def match_template(img_src, img_template, threshold=0.9):
    # we remove alpha channel if exists
    img_src = img_src[:, :, :3]
    img_template = img_template[:, :, :3]

    res = cv2.matchTemplate(img_src, img_template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, _ = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # change threshold in order to return only the different instances
        threshold = max(threshold, max_val - 0.01)

        loc = np.where(res >= threshold)

        return list(zip(*loc[::-1]))
    else:
        return []


def find_elements_by_image(self, filename):
    """
    Locate all the occurence of an image in the webpage.

    :Args:
        - filename: The path to the image to search (image shall be in PNG format).

    Returns:
        A list of ImageElement.
    """
    template = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    template_height, template_width, _ = template.shape

    webpage_png = self.get_screenshot_as_png()
    webpage_img = Image.open(io.BytesIO(webpage_png))
    webpage = np.asarray(webpage_img, dtype=np.float32).astype(np.uint8)
    webpage = cv2.cvtColor(webpage, cv2.COLOR_BGR2RGB)

    return [
        ImageElement(self, loc[0], loc[1], template_width, template_height)
        for loc in match_template(webpage, template)
    ]


def find_element_by_image(self, filename):
    """
    Locate an image in the webpage.

    :Args:
        - filename: The path to the image to search (image shall be in PNG format).

    Returns:
        An ImageElement.
    """
    implicit_wait = ImplicitWait()
    implicit_wait.start()

    elements = find_elements_by_image(self, filename)

    while len(elements) == 0 and not implicit_wait.max_time_exceeded:
        elements = find_elements_by_image(self, filename)

    if len(elements) == 0:
        raise NoSuchElementException(
            'Unable to locate element: [image="{filename}"]'.format(filename=filename)
        )
    else:
        return elements[0]
