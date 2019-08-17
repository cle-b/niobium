# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import pytest
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotInteractableException,
)


def test_web_element_need_wait(selenium, website):
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    with pytest.raises(ElementNotVisibleException):
        selenium.find_element_by_id("button_displayed_enabled").wait()
    with pytest.raises(ElementNotInteractableException):
        selenium.find_element_by_id("button_displayed_disabled").wait(
            displayed=None, enabled=True
        )
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_id("button_always_displayed_enabled").wait(
            displayed=False, enabled=None
        )
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_id("button_always_displayed_enabled").wait(
            displayed=None, enabled=False
        )


def test_web_element_wait_displayed_implict(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_id("button_displayed_enabled").wait(
        displayed=True, enabled=None
    )


def test_web_element_wait_enabled_implict(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_id("button_displayed_enabled").wait(
        displayed=None, enabled=True
    )


def test_web_element_wait_displayed_explicit(selenium, website):
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_id("button_displayed_enabled").wait(
        displayed=True, enabled=None, timeout=6
    )


def test_web_element_wait_enabled_explicit(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_id("button_displayed_enabled").wait(None, True, 6)


def test_web_element_wait_displayed_then_click(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_id("button_displayed_enabled").wait().click()
    assert (
        selenium.find_element_by_id("message").text == "button_displayed_enabled"
    ), "click on element failed"
