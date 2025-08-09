import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class ImplicitWait(object):
    time_to_wait: float = 0

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    @property
    def max_time_exceeded(self):
        return (time.time() - self.start_time) > self.time_to_wait


_real_implicitly_wait = webdriver.remote.webdriver.WebDriver.implicitly_wait


def _patch_implicitly_wait(self: WebDriver, time_to_wait: float):
    ImplicitWait.time_to_wait = time_to_wait
    return _real_implicitly_wait(self, time_to_wait)


class ExplicitWait(object):
    def __init__(self, time_to_wait):
        self.start_time = None
        self.time_to_wait = time_to_wait

    def start(self):
        self.start_time = time.time()

    @property
    def max_time_exceeded(self):
        return (time.time() - self.start_time) > self.time_to_wait
