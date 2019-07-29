# -*- coding: utf-8 -*-
from urllib.parse import urljoin


def test_find_elements_by_image_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser0.png")) == 0


def test_find_elements_by_image_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser_edge.png")) == 1


def test_find_elements_by_image_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser_firefox.png")) == 3


def test_find_elements_by_image_one_element_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    elements = selenium.find_elements_by_image("tests/html/browser_edge.png")
    assert len(elements) == 1
    elements[0].click()
    assert (
        selenium.find_element_by_id("message").text == "edge1"
    ), "click on element failed"


def test_find_elements_by_image_three_elements_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    elements = selenium.find_elements_by_image("tests/html/browser_firefox.png")
    assert len(elements) == 3
    messages = []
    for element in elements:
        element.click()
        messages.append(selenium.find_element_by_id("message").text)
    messages.sort()
    assert messages == ["firefox1", "firefox2", "firefox3"], "click on element failed"
