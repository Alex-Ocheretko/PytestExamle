from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import base_page_locators
from page_object.base_page import BasePage


class HomePage(BasePage):

    def click_forms_button(self):
        self.click(base_page_locators.FORMS_BUTTON, 10)

    def close_fixedban_if_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(base_page_locators.CLOSE_FIXEDBAN_BUTTON)
            ).click()
        except TimeoutException:
            pass
