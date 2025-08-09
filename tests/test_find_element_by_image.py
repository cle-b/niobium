from urllib.parse import urljoin

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_find_element_by_image_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element(By.IMAGE, "tests/html/browser0.png")


def test_find_element_by_image_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")


def test_find_element_by_image_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    selenium.find_element(By.IMAGE, "tests/html/browser_firefox.png")


def test_find_element_by_image_one_element_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    element = selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")
    element.click()
    assert (
        selenium.find_element(By.ID, "message").text == "edge1"
    ), "click on element failed"


def test_find_element_by_image_one_element_click_at(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    element = selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")
    element.click_at(-100, 200)
    assert (
        selenium.find_element(By.ID, "message").text == "firefox2"
    ), "click on element failed"


def test_find_element_by_image_one_element_move_to(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    element = selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")
    element.move_to()
    assert (
        selenium.find_element(By.ID, "message").text == "overedge1"
    ), "click on element failed"


def test_find_element_by_image_one_element_move_at(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    element = selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")
    element.move_at(200, 200)
    assert (
        selenium.find_element(By.ID, "message").text == "overchrome2"
    ), "click on element failed"


def test_find_element_by_image_one_element_need_wait(selenium, website):
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")


def test_find_element_by_image_one_element_with_wait(selenium, website):
    selenium.implicitly_wait(6)
    selenium.get(urljoin(website, "/browsers_delay.htm"))
    selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")


def test_find_element_by_image_click_need_scroll(selenium, website):
    selenium.get(urljoin(website, "/browsers_scroll.htm"))
    with pytest.raises(NoSuchElementException):
        selenium.find_element(By.IMAGE, "tests/html/browser_edge.png")


def test_find_element_by_image_click_with_scroll(selenium, website):
    selenium.get(urljoin(website, "/browsers_scroll.htm"))
    img_browsers = selenium.find_element(By.ID, "browsers")
    selenium.execute_script("arguments[0].scrollIntoView();", img_browsers)
    selenium.find_element(By.IMAGE, "tests/html/browser_edge.png").click()
    assert (
        selenium.find_element(By.ID, "message").text == "edge1"
    ), "click on element failed"


def test_find_element_not_by_image(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    for id in ["fe1", "fe2"]:
        selenium.find_element(By.ID, id).click()
        assert (
            selenium.find_element(By.ID, "message").text == id
        ), "click on element failed"
