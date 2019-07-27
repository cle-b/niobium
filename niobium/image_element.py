# -*- coding: utf-8 -*-
from selenium import webdriver


class ImageElement(object):
    def __init__(self, parent, location, size):
        self.parent = parent
        self.location = location
        self.size = size
        self.rect = None  # TODO

    def click(self, position=None):
        action = webdriver.common.action_chains.ActionChains(self.parent)
        if position is None:
            position = (
                self.location[0] + self.size[0] / 2,
                self.location[1] + self.size[1] / 2,
            )
        action.move_by_offset(position[0], position[1])
        action.click()
        action.perform()
