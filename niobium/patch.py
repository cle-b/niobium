from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common import by

from niobium.find_image import By as NiobiumBy
from niobium.find_image import find_element
from niobium.find_image import find_elements
from niobium.timeout import _patch_implicitly_wait
from niobium.webelement_action import click_at, move_to, move_at
from niobium.webelement_wait import wait


def patch_image():

    by.By = NiobiumBy

    WebDriver.find_element = find_element
    WebDriver.find_elements = find_elements


def patch_timeout():
    WebDriver.implicitly_wait = _patch_implicitly_wait


def patch_webelement_action():
    if "click_at" not in dir(WebElement):
        WebElement.click_at = click_at

    if "move_to" not in dir(WebElement):
        WebElement.move_to = move_to

    if "move_at" not in dir(WebElement):
        WebElement.move_at = move_at


def patch_webelement_wait():
    if "wait" not in dir(WebElement):
        WebElement.wait = wait
