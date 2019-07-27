# -*- coding: utf-8 -*-
from urllib.parse import urljoin


def test_find_elements_by_image_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser0.png")) == 0


def test_find_elements_by_image_one_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser_edge.png")) == 1


def test_find_elements_by_image_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_elements_by_image("tests/html/browser_firefox.png")) == 3
