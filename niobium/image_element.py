# -*- coding: utf-8 -*-
from selenium import webdriver


class ImageElement(object):
    def __init__(self, parent, location, size):
        if not isinstance(
            parent,
            (
                webdriver.remote.webelement.WebElement,
                webdriver.remote.webdriver.WebDriver,
            ),
        ):
            raise TypeError("parent shall a WebElement or a WebDriver")
        self.parent = parent
        self.location = location
        self.size = size
        self.rect = None  # TODO

    def click(self, position=None):
        if position is None:
            position = (
                self.location[0] + self.size[0] / 2,
                self.location[1] + self.size[1] / 2,
            )

        if isinstance(self.parent, webdriver.remote.webdriver.WebDriver):
            action = webdriver.common.action_chains.ActionChains(self.parent)
            offset_element = self.__get_element_top_left()
        else:
            action = webdriver.common.action_chains.ActionChains(self.parent.parent)
            offset_element = self.parent

        action.move_to_element_with_offset(offset_element, position[0], position[1])
        action.click()
        action.perform()

    def __get_element_top_left(self):
        # create an empty element at the corner top left of the webpage in order to be
        # able to click in the good position even if the page is scrolled
        if isinstance(self.parent, webdriver.remote.webdriver.WebDriver):
            javacript_create_topleft_element = """
            if(! document.getElementById("niobium-topleft-elt"))
            {
                var topleft_elt = document.createElement("div");
                topleft_elt.style.top=0;
                topleft_elt.style.left=0;
                topleft_elt.style.height=0;
                topleft_elt.style.width=0;
                topleft_elt.style.margin=0;
                topleft_elt.style.padding=0;
                topleft_elt.style.position="fixed";
                topleft_elt.id="niobium-topleft-elt";
                document.body.appendChild(topleft_elt);
            }
            """
            self.parent.execute_script(javacript_create_topleft_element)
            return self.parent.find_element_by_id("niobium-topleft-elt")
