# ImageElement

Niobium adds computer vision to Selenium.

## Locate an image in the page

You can locate an image in the page using the following method:

    find_element_by_image(filename)

And to find multiple images (this method returns a list)

    find_elements_by_image(filename)

These methods have the same behavior than the classic find_element methods but they return an ImageElement instead of a WebElement.

They take only one argument which is the path to the PNG image that you search.

## Find element by image

The methods find_element_by_image and find_elements_by_image are available only from the WebDriver object. Only the visible page is analyzed in order to locate the image.

    # -*- coding: utf-8 -*-
    from selenium import webdriver
    import niobium # noqa: F401

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org/")
   
    driver.find_element_by_image("logo_python.png")

    driver.quit()

## Click on the image

You can click on the element.

    driver.find_element_by_image("logo_python.png").click()

By default, the click is performed on the center of the element.

## Click with offset

You can click to a specific location related to the top left corner of the element with the `click_at(xoffset, yoffset)` function.

    driver.find_element_by_image("logo_python.png").click_at(100, -100) 

## Move the cursor over the element

You can move the cursor to the center of the element with the `move_to()` function.

    driver.find_element_by_image("logo_python.png").move_to()

## Move the cursor with offset

You can move the cursor to a specific location related to the top left corner of the element with the `move_at(xoffset, yoffset)` function.

    driver.find_element_by_image("logo_python.png").move_at(20, 20)


