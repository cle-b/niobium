# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver

from .find_image import find_element_by_image, find_elements_by_image

from .timeout import _patch_implicitly_wait


def patch_image():
    if "find_element_by_image" not in dir(WebDriver):
        WebDriver.find_element_by_image = find_element_by_image

    if "find_elements_by_image" not in dir(WebDriver):
        WebDriver.find_elements_by_image = find_elements_by_image


def patch_timeout():
    WebDriver.implicitly_wait = _patch_implicitly_wait
