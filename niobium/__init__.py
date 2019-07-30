# -*- coding: utf-8 -*-
import selenium
from .patch import patch_image, patch_timeout, patch_webelement_action

patch_image()
patch_timeout()
patch_webelement_action()

__all__ = ["selenium"]
