# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .find_image import find_element_by_image, find_elements_by_image

from .timeout import _patch_implicitly_wait

from .webelement_action import click_at, move_to, move_at


def patch_image():
    if "find_element_by_image" not in dir(WebDriver):
        WebDriver.find_element_by_image = find_element_by_image

    if "find_elements_by_image" not in dir(WebDriver):
        WebDriver.find_elements_by_image = find_elements_by_image


def patch_timeout():
    WebDriver.implicitly_wait = _patch_implicitly_wait


def patch_webelement_action():
    if "click_at" not in dir(WebElement):
        WebElement.click_at = click_at

    if "move_to" not in dir(WebElement):
        WebElement.move_to = move_to

    if "move_at" not in dir(WebElement):
        WebElement.move_at = move_at
