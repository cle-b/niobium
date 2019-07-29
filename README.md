[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black) [![Build Status](https://travis-ci.org/cle-b/niobium.svg?branch=master)](https://travis-ci.org/cle-b/niobium) 

# Niobium

Niobium extends the Python Selenium client with nice features.

## Why Niobium

Selenium is probably the better tool for web automation. But sometimes it's hard to write a clean automation script. 

With Niobium you can keep using Selenium and simplify your scripts. For example, Niobium add a new element locator, find_element_by_image, which add image recognition capacity in order to find an element in the webpage.

The goal of Niobium is not to replace Selenium. We only want to add to Selenium the functions we will love to see in Selenium natively.

Niobium philosophy is to keep as simple as possible.

## Installation

Niobium is available on Pypi, so simply use pip.

    pip install niobium

## Getting Started

In order to use Niobium, you just need to import it in your script. Selenium will be automatically extended. 

    # -*- coding: utf-8 -*-
    from selenium import webdriver
    import niobium

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org/")
   
    driver.find_element_by_image("logo_python.png")

    driver.quit()

In order to avoid warning with your linter, you can import selenium from niobium.

    # -*- coding: utf-8 -*-
    from niobium import selenium

    driver = selenium.webdriver.Firefox()
    ...

or simply disable the warning, like in this example for flake8

    # -*- coding: utf-8 -*-
    from selenium import webdriver
    import niobium  # noqa: F401

    driver = webdriver.Firefox()
    ...

If you use pytest and especially pytest-selenium, just import niobium in your conftest.py.

## Documentation

[https://niobium.readthedocs.io/](https://niobium.readthedocs.io/)

## Warnings

Some features implemented in Niobium are here only to help you when there is no other easy solution. If you do a bad usage of Niobium features, it can result to a bad perform in your script, or it will be difficult to maintain it. Please read the documentation in order to know the special warnings for the use of these features.

Niobium do not modify the Selenium library. The patches are only applied at runtime.