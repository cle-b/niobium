# WebElement new actions

Niobium make easier the mouse action on a `WebElement`.

## Click with offset

You can click to a specific location related to the top left corner of the element with the `click_at(xoffset, yoffset)` function.

```python
    driver.find_element(By.ID, "myelt").click_at(100, -100) 
```

## Move the cursor over the element

You can move the cursor to the center of the element with the `move_to()` function.

```python
    driver.find_element(By.ID, "myelt").move_to()
```

## Move the cursor with offset

You can move the cursor to a specific location related to the top left corner of the element with the `move_at(xoffset, yoffset)` function.

```python
    driver.find_element(By.ID, "myelt").move_at(20, 20)
```