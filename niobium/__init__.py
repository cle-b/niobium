# -*- coding: utf-8 -*-
import selenium
from .patch import patch_image, patch_timeout

patch_image()
patch_timeout()

__all__ = ["selenium"]
