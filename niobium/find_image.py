import io
from typing import Optional
from typing import Union


import cv2
import numpy as np
from PIL import Image
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By as OriginalBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


from niobium.image_element import ImageElement
from niobium.timeout import ImplicitWait

original_webdriver_find_element = WebDriver.find_element
original_webdriver_find_elements = WebDriver.find_elements


class By(OriginalBy):
    IMAGE = "image"


def match_template(img_src, img_template, threshold=0.9):
    # we remove alpha channel if exists
    img_src = img_src[:, :, :3]
    img_template = img_template[:, :, :3]

    res = cv2.matchTemplate(img_src, img_template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, _ = cv2.minMaxLoc(res)

    if max_val >= threshold:
        # change threshold in order to return only the different instances
        threshold = max(threshold, max_val - 0.01)

        loc = np.where(res >= threshold)

        return list(zip(*loc[::-1]))
    else:
        return []


def find_elements_by_image(self: WebDriver, filename: str) -> list[ImageElement]:
    """
    Locate all the occurence of an image in the webpage.

    :Args:
        - filename: The path to the image to search (image shall be in PNG format).

    :Returns:
        A list of ImageElement.
    """
    template = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    if template is None:
        raise WebDriverException(f"Unable to read {filename}")
    template_height, template_width, _ = template.shape

    webpage_png = self.get_screenshot_as_png()
    webpage_img = Image.open(io.BytesIO(webpage_png))
    webpage: np.ndarray = np.asarray(webpage_img, dtype=np.float32).astype(np.uint8)
    webpage = cv2.cvtColor(webpage, cv2.COLOR_BGR2RGB)

    return [
        ImageElement(self, loc[0], loc[1], template_width, template_height)
        for loc in match_template(webpage, template)
    ]


def find_element_by_image(self: WebDriver, filename: str) -> ImageElement:
    """
    Locate an image in the webpage.

    :Args:
        - filename: The path to the image to search (image shall be in PNG format).

    :Returns:
        An ImageElement.

    :Raises:
        - NoSuchElementException - if the element wasn't found
    """
    implicit_wait = ImplicitWait()
    implicit_wait.start()

    elements = find_elements_by_image(self, filename)

    while len(elements) == 0 and not implicit_wait.max_time_exceeded:
        elements = find_elements_by_image(self, filename)

    if len(elements) == 0:
        raise NoSuchElementException(
            'Unable to locate element: [image="{filename}"]'.format(filename=filename)
        )
    else:
        return elements[0]


def find_element(
    self: WebDriver, by=By.ID, value: Optional[str] = None
) -> Union[WebElement, ImageElement]:
    if by == By.IMAGE and value is not None:
        return find_element_by_image(self, value)
    else:
        return original_webdriver_find_element(self, by, value)


def find_elements(
    self: WebDriver, by=By.ID, value: Optional[str] = None
) -> Union[list[WebElement], list[ImageElement]]:
    if by == By.IMAGE and value is not None:
        return find_elements_by_image(self, value)
    else:
        return original_webdriver_find_elements(self, by, value)
