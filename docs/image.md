# ImageElement

Niobium adds computer vision to Selenium.

## Locate an image in the page

You can locate an image in the page using the following method:

    find_element_by_image

And to find multiple images (this method returns a list)

    find_elements_by_image

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

## Move the mouse over the image

You can move the cursor to the element.

    driver.find_element_by_image("logo_python.png").move_to()

By default, the cursor is move to the center of the element but you can choose a specific location for the cursor.

    driver.find_element_by_image("logo_python.png").move_to(100, 100)

## Click on the image

You can click on the element.

    driver.find_element_by_image("logo_python.png").click()

By default, the click is perform on the center of the element but you can choose a specific location for the click. It can be inside or outside the element.

    driver.find_element_by_image("logo_python.png").click(-10, -10)
