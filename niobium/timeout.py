# -*- coding: utf-8 -*-
import time

from selenium import webdriver


class ImplicitWait(object):
    time_to_wait = 0

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    @property
    def max_time_exceeded(self):
        return (time.time() - self.start_time) > self.time_to_wait


_real_implicitly_wait = webdriver.remote.webdriver.WebDriver.implicitly_wait


def _patch_implicitly_wait(self, time_to_wait):
    ImplicitWait.time_to_wait = time_to_wait
    return _real_implicitly_wait(self, time_to_wait)
