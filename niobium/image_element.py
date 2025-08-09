from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Dict
from typing import Union


class ImageElement(object):
    def __init__(
        self, parent: WebDriver, x: int, y: int, width: int, height: int
    ) -> None:
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
    def parent(self) -> WebDriver:
        """Internal reference to the WebDriver instance this element was found from."""
        return self._parent

    @property
    def location(self) -> Dict[str, int]:
        """The location of the element in the renderable canvas."""
        return self._location

    @property
    def size(self) -> Dict[str, int]:
        """The size of the element."""
        return self._size

    @property
    def rect(self) -> Dict[str, int]:
        """A dictionary with the size and location of the element."""
        return self._rect

    def move_to(self) -> None:
        """
        Move the mouse to the center of the specified element.
        """
        self.__move_and_click(None, None, False)

    def move_at(self, xoffset: int, yoffset: int) -> None:
        """
        Move the mouse by an offset of the specified element.
           Offsets are relative to the top-left corner of the element.

        :Args:
         - xoffset: X offset to move to.
         - yoffset: Y offset to move to.
        """
        self.__move_and_click(xoffset, yoffset, False)

    def click(self) -> None:
        """
        Move the mouse to the center of the specified element and click.
        """
        self.__move_and_click(None, None, True)

    def click_at(self, xoffset: int, yoffset: int) -> None:
        """
        Move the mouse by an offset of the specified element and click.
           Offsets are relative to the top-left corner of the element.

        :Args:
         - xoffset: X offset to move to.
         - yoffset: Y offset to move to.
        """
        self.__move_and_click(xoffset, yoffset, True)

    def __move_and_click(
        self,
        xoffset: Union[int, None] = None,
        yoffset: Union[int, None] = None,
        click: bool = False,
    ) -> None:
        if xoffset is None:
            xoffset = self.location["x"] + int(self.size["width"] / 2)
        else:
            xoffset = self.location["x"] + xoffset

        if yoffset is None:
            yoffset = self.location["y"] + int(self.size["height"] / 2)
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
        return self.parent.find_element(By.ID, "niobium-topleft-elt")
