# -*- coding: utf-8 -*-
from selenium import webdriver


class ImageElement(object):
    def __init__(self, parent, x, y, width, height):
        """
        Create a new ImageElement.

        :Args:
         - parent: The WebDriver.
         - x: location of the element on the X axis.
         - y: location of the element on the Y axis.
         - width: the width of the element.
         - height: the height of the element.
        """
        self._parent = parent
        self._location = {"x": x, "y": y}
        self._size = {"width": width, "height": height}
        self._rect = {"x": x, "y": y, "width": width, "height": height}

    @property
    def parent(self):
        """Internal reference to the WebDriver instance this element was found from."""
        return self._parent

    @property
    def location(self):
        """The location of the element in the renderable canvas."""
        return self._location

    @property
    def size(self):
        """The size of the element."""
        return self._size

    @property
    def rect(self):
        """A dictionary with the size and location of the element."""
        return self._rect

    def move_to(self):
        """
        Move the mouse to the center of the specified element.
        """
        self.__move_and_click(None, None, False)

    def move_at(self, xoffset, yoffset):
        """
        Move the mouse by an offset of the specified element.
           Offsets are relative to the top-left corner of the element.

        :Args:
         - xoffset: X offset to move to.
         - yoffset: Y offset to move to.
        """
        self.__move_and_click(xoffset, yoffset, False)

    def click(self):
        """
        Move the mouse to the center of the specified element and click.
        """
        self.__move_and_click(None, None, True)

    def click_at(self, xoffset, yoffset):
        """
        Move the mouse by an offset of the specified element and click.
           Offsets are relative to the top-left corner of the element.

        :Args:
         - xoffset: X offset to move to.
         - yoffset: Y offset to move to.
        """
        self.__move_and_click(xoffset, yoffset, True)

    def __move_and_click(self, xoffset=None, yoffset=None, click=False):
        if xoffset is None:
            xoffset = self.location["x"] + self.size["width"] / 2
        else:
            xoffset = self.location["x"] + xoffset

        if yoffset is None:
            yoffset = self.location["y"] + self.size["height"] / 2
        else:
            yoffset = self.location["y"] + yoffset

        action = webdriver.common.action_chains.ActionChains(self.parent)
        offset_element = self.__get_element_top_left()
        action.move_to_element_with_offset(offset_element, xoffset, yoffset)
        if click:
            action.click()
        action.perform()

    def __get_element_top_left(self):
        # create an empty element at the corner top left of the webpage in order to be
        # able to click in the good position even if the page is scrolled
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
