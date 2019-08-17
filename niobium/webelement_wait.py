# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotInteractableException,
    NoSuchElementException,
)

from .timeout import ImplicitWait, ExplicitWait


def wait(self, displayed=True, enabled=True, timeout=None):
    """
    Wait until expected conditions.

    :Args:
        - displayed (bool - default: True): Wait until the element is displayed.
        - enabled  (bool - default: True): Wait until the element is enabled.
        - timeout  (bool - default: None): Timeout in seconds, implicit timeout if None.

    :Returns:
        The element itself.

    :Raises:
         - ElementNotVisibleException - if element is not visible.
         - ElementNotInteractableException - if element is not enabled.
         - NoSuchElementException - if expected conditions not satisfied.
    """
    wait_timer = ExplicitWait(timeout) if timeout is not None else ImplicitWait()
    wait_timer.start()

    once = True
    while (not wait_timer.max_time_exceeded) or once:
        once = False
        if ((displayed is None) or (displayed == self.is_displayed())) and (
            (enabled is None) or (enabled == self.is_enabled())
        ):
            return self
        time.sleep(0.2)

    if displayed:
        raise ElementNotVisibleException()
    elif enabled:
        raise ElementNotInteractableException()
    else:
        raise NoSuchElementException()
