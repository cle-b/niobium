# -*- coding: utf-8 -*-
from urllib.parse import urljoin


def test_webelement_click_at(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element_by_id("beta").click_at(20, 20)
    assert (
        selenium.find_element_by_id("message").text == "beta"
    ), "click on element failed"
    selenium.find_element_by_id("lite").click_at(-170, -170)
    assert (
        selenium.find_element_by_id("message").text == "firefox"
    ), "click on element failed"


def test_webelement_move_to(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element_by_id("developer").move_to()
    assert (
        selenium.find_element_by_id("message").text == "overdeveloper"
    ), "click on element failed"


def test_webelement_move_at(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element_by_id("developer").move_at(100, -100)
    assert (
        selenium.find_element_by_id("message").text == "overfirefox"
    ), "click on element failed"
