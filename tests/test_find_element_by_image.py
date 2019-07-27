# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import pytest
from selenium.common.exceptions import NoSuchElementException


def test_find_element_by_image_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element_by_image("tests/html/browser0.png")


def test_find_element_by_image_one_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element_by_image("tests/html/browser1.png")


def test_find_element_by_image_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element_by_image("tests/html/browser3.png")
