from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.constants import DEFAULT_EXPLICIT_WAIT
from core.decorators import handle_none_argument


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @handle_none_argument
    def click(self, locator: tuple[str, str], time: int = DEFAULT_EXPLICIT_WAIT) -> None:
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    @handle_none_argument
    def get_text(self, locator: tuple[str, str], time: int = DEFAULT_EXPLICIT_WAIT) -> str:
        text = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).text
        return text

    @handle_none_argument
    def send_keys(self, locator: tuple[str, str], keys: str or int, time: int = DEFAULT_EXPLICIT_WAIT,
                  press_enter: bool = False) -> None:
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))
        element.send_keys(keys)
        if press_enter:
            element.send_keys(Keys.ENTER)

    @handle_none_argument
    def value_of_css_property(self, locator: tuple[str, str], property_name, time: int = DEFAULT_EXPLICIT_WAIT) -> str:
        value = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).value_of_css_property(f"{property_name}")
        return value
