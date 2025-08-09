# WebElement excpected conditions

Niobium make easier the waiting of expected conditions on a `WebElement`.

## Wait until element is displayed and enabled

You just have to call the `wait()` function on a `WebElement`. 

```python
    driver.find_element(By.ID, "myelt").wait()
```

By default, the timeout is the same the implicitly_wait timeout.

## Wait using a specific timeout

You can specify the maximum time to wait using the `timeout` argument (in seconds).

```python
    driver.find_element(By.ID, "myelt").wait(timeout=5)
```

## Choose expected conditions to wait

You can choose which expected conditions to wait. 

Two expected conditions are available: 

  - displayed
  - enabled

If value is None, the expected condition is not checked.

```python
    driver.find_element(By.ID, "myelt").wait(displayed=False,  enabled=False)

    driver.find_element(By.ID, "myelt").wait(enabled=False)
```

## Chain action after wait()

You can chain all available actions after the wait.

```python
    driver.find_element(By.ID, "myelt").wait(timeout=5).click()
```

It's usefull when you have to wait until an element is visible before to click on it.