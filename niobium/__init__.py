import selenium
from .patch import (
    patch_image,
    patch_timeout,
    patch_webelement_action,
    patch_webelement_wait,
)

patch_image()
patch_timeout()
patch_webelement_action()
patch_webelement_wait()

__all__ = ["selenium"]

__version__ = "0.4.0"
