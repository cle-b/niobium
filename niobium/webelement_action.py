from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from typing import Union


def move_to(self: WebElement):
    """
    Move the mouse to the center of the specified element.
    """
    __web_element_move_and_click(self, None, None, False)


def move_at(self: WebElement, xoffset: int, yoffset: int):
    """
    Move the mouse by an offset of the specified element.
        Offsets are relative to the top-left corner of the element.

    :Args:
        - xoffset: X offset to move to.
        - yoffset: Y offset to move to.
    """
    __web_element_move_and_click(self, xoffset, yoffset, False)


def click_at(self: WebElement, xoffset: int, yoffset: int):
    """
    Move the mouse by an offset of the specified element and click.
        Offsets are relative to the top-left corner of the element.

    :Args:
        - xoffset: X offset to move to.
        - yoffset: Y offset to move to.
    """
    __web_element_move_and_click(self, xoffset, yoffset, True)


def __web_element_move_and_click(
    webelement: WebElement,
    xoffset: Union[int, None],
    yoffset: Union[int, None],
    click: bool,
):
    action = webdriver.common.action_chains.ActionChains(webelement.parent)
    if xoffset is None or yoffset is None:
        action.move_to_element(webelement)
    else:
        action.move_to_element_with_offset(webelement, xoffset, yoffset)
    if click:
        action.click()
    action.perform()
