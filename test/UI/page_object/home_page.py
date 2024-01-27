from selenium.webdriver.common.by import By

from test.UI.page_object.base_page import BasePage


FORMS_BUTTON = (By.XPATH, "//h5[text()='Forms']")


class HomePage(BasePage):

    def click_forms_button(self):
        self.click(FORMS_BUTTON)
