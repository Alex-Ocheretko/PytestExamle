from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.base_utils import DEFAULT_EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator: tuple[str, str], time: int = DEFAULT_EXPLICIT_WAIT):
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator: tuple[str, str], time: int = DEFAULT_EXPLICIT_WAIT) -> str:
        text = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).text
        return text

    def send_keys(self, locator: tuple[str, str], keys: str or int, time: int = DEFAULT_EXPLICIT_WAIT):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).send_keys(keys)

    def value_of_css_property(self, locator: tuple[str, str], property_name, time: int = DEFAULT_EXPLICIT_WAIT):
        value = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).value_of_css_property(f"{property_name}")
        return value

    @staticmethod
    def replace_placeholders_in_locator(locator: tuple[str, str], replacement: list or str) -> tuple[str, str]:
        if isinstance(replacement, list):
            for item in replacement:
                locator = (locator[0], locator[1].replace('{}', str(item)))
        else:
            locator = (locator[0], locator[1].replace('{}', str(replacement)))

        return locator
