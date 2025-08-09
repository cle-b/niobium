from urllib.parse import urljoin

from selenium.webdriver.common.by import By


def test_find_images_no_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_images("tests/html/browser0.png")) == 0


def test_find_images_one_element(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_images("tests/html/browser_edge.png")) == 1


def test_find_images_three_elements(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    assert len(selenium.find_images("tests/html/browser_firefox.png")) == 3


def test_find_images_one_element_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    elements = selenium.find_images("tests/html/browser_edge.png")
    assert len(elements) == 1
    elements[0].click()
    assert (
        selenium.find_element(By.ID, "message").text == "edge1"
    ), "click on element failed"


def test_find_images_three_elements_click(selenium, website):
    selenium.get(urljoin(website, "/browsers.htm"))
    elements = selenium.find_images("tests/html/browser_firefox.png")
    assert len(elements) == 3
    messages = []
    for element in elements:
        element.click()
        messages.append(selenium.find_element(By.ID, "message").text)
    messages.sort()
    assert messages == ["firefox1", "firefox2", "firefox3"], "click on element failed"
