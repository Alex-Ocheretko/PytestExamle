from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.base_utils import BASE_TIME_OUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, time: int = BASE_TIME_OUT):
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator, time: int = BASE_TIME_OUT):
        text = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).text
        return text

    def send_keys(self, locator, keys, time: int = BASE_TIME_OUT):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).send_keys(keys)

    def value_of_css_property(self, locator, property_name, time: int = BASE_TIME_OUT):
        value = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        ).value_of_css_property(f"{property_name}")
        return value
