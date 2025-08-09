# ImageElement

Niobium adds computer vision to Selenium.

## Locate an image in the page

You can locate an image in the page using the following method:

```python
    find_element(By.IMAGE, filename)
```

And to find multiple images (this method returns a list)

```python
    find_elements(By.IMAGE, filename)
```

These methods have the same behavior than the classic `find_element` methods but they return an `ImageElement` instead of a `WebElement` if you use the By.IMAGE selector.

They take only one argument which is the path to the PNG image that you search.

## Find element by image

The methods `find_element` and `find_elements` using the selector `By.IMAGE` are available only from the `WebDriver` object. Only the visible page is analyzed in order to locate the image.

```python
    from selenium import webdriver
    import niobium # noqa: F401

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org/")
   
    driver.find_element(By.IMAGE, "logo_python.png")

    driver.quit()
```

## Click on the image

You can click on the element.

```python
    driver.find_element(By.IMAGE, "logo_python.png").click()
```

By default, the click is performed on the center of the element.

## Click with offset

You can click to a specific location related to the top left corner of the element with the `click_at(xoffset, yoffset)` function.

```python
    driver.find_element(By.IMAGE, "logo_python.png").click_at(100, -100) 
```

## Move the cursor over the element

You can move the cursor to the center of the element with the `move_to()` function.

```python
    driver.find_element(By.IMAGE, "logo_python.png").move_to()
```

## Move the cursor with offset

You can move the cursor to a specific location related to the top left corner of the element with the `move_at(xoffset, yoffset)` function.

```python
    driver.find_element(By.IMAGE, "logo_python.png").move_at(20, 20)
```
