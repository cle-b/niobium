from urllib.parse import urljoin

from selenium.webdriver.common.by import By


def test_webelement_click_at(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element(By.ID, "beta").click_at(20, 20)
    assert (
        selenium.find_element(By.ID, "message").text == "beta"
    ), "click on element failed"
    selenium.find_element(By.ID, "lite").click_at(-170, -170)
    assert (
        selenium.find_element(By.ID, "message").text == "firefox"
    ), "click on element failed"


def test_webelement_move_to(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element(By.ID, "developer").move_to()
    assert (
        selenium.find_element(By.ID, "message").text == "overdeveloper"
    ), "click on element failed"


def test_webelement_move_at(selenium, website):
    selenium.get(urljoin(website, "/elements.htm"))
    selenium.find_element(By.ID, "firefox").move_at(40, 40)
    assert (
        selenium.find_element(By.ID, "message").text == "overfirefox"
    ), "click on element failed"
    selenium.find_element(By.ID, "lite").move_at(100, -300)
    assert (
        selenium.find_element(By.ID, "message").text == "overbeta"
    ), "click on element failed"
    selenium.find_element(By.ID, "developer").move_at(300, 10)
    assert (
        selenium.find_element(By.ID, "message").text == "overlite"
    ), "click on element failed"
