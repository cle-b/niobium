# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import pytest
from selenium.common.exceptions import NoSuchElementException


def test_find_element_by_image_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_image("tests/html/browser0.png")


def test_find_element_by_image_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element_by_image("tests/html/browser_edge.png")


def test_find_element_by_image_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element_by_image("tests/html/browser_firefox.png")


def test_find_element_by_image_one_element_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    element = selenium.find_element_by_image("tests/html/browser_edge.png")
    element.click()
    assert (
        selenium.find_element_by_id("message").text == "edge1"
    ), "click on element failed"


def test_find_element_by_image_one_element_need_wait(selenium, website):
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_image("tests/html/browser_edge.png")


def test_find_element_by_image_one_element_with_wait(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element_by_image("tests/html/browser_edge.png")


def test_find_element_by_image_click_need_scroll(selenium, website):
    selenium.get(urljoin(website, "/browsers_scroll.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_image("tests/html/browser_edge.png")


def test_find_element_by_image_click_with_scroll(selenium, website):
    selenium.get(urljoin(website, "/browsers_scroll.htm"))
    img_browsers = selenium.find_element_by_id("browsers")
    selenium.execute_script("arguments[0].scrollIntoView();", img_browsers)
    selenium.find_element_by_image("tests/html/browser_edge.png")


def test_find_element_by_image_from_element_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers_element.htm"))
    selenium.find_element_by_image("tests/html/browser_edge.png")
    selenium.find_element_by_id("container1").find_element_by_image(
        "tests/html/browser_edge.png"
    )


def test_find_element_by_image_from_element_click_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers_element.htm"))
    selenium.find_element_by_image("tests/html/browser_edge.png")
    selenium.find_element_by_id("container1").find_element_by_image(
        "tests/html/browser_edge.png"
    ).click()
    assert (
        selenium.find_element_by_id("message").text == "edge1-container1"
    ), "click on element failed"
    selenium.find_element_by_id("container2").find_element_by_image(
        "tests/html/browser_edge.png"
    ).click()
    assert (
        selenium.find_element_by_id("message").text == "edge1-container2"
    ), "click on element failed"
