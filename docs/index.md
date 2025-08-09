# Welcome to the Niobium documentation

Niobium extends the Python Selenium client with nice features.

## Why Niobium

Selenium is a good tool for web automation, but sometimes it's hard to write a clean automation script.

With Niobium, you can keep using Selenium while simplifying your scripts. For example, Niobium adds a new element locator,` By.IMAGE`, which enables image recognition in `WebDriver.find_element` to locate an element on the webpage.

The goal of Niobium is not to replace Selenium. We only want to add to Selenium the functions we will love to see in Selenium natively.

Niobium philosophy is to keep as simple as possible.

## Installation

Niobium is available on Pypi, so simply use pip.

    pip install niobium

## Getting Started

In order to use Niobium, you just need to import it in your script. Selenium will be automatically extended. 

```python
    from selenium import webdriver
    import niobium

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org/")
   
    driver.find_element(By.IMAGE, "logo_python.png")

    driver.quit()
```

In order to avoid warning with your linter, you can import selenium from niobium.

```python
    from niobium import selenium

    driver = selenium.webdriver.Firefox()
    ...
```

or simply disable the warning, like in this example for flake8

```python
    from selenium import webdriver
    import niobium  # noqa: F401

    driver = webdriver.Firefox()
    ...
```

If you use *pytest* and especially *pytest-selenium*, just import niobium in your `conftest.py`.

## Warnings

Some features implemented in Niobium are here only to help you when there is no other easy solution. If you do a bad usage of Niobium features, it can result to a bad performance in your script, or it will be difficult to maintain it. Please read the documentation in order to know the special warnings for the use of these features.

Niobium do not modify the Selenium library package. The patches are only applied at runtime.