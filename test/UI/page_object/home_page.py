from test.UI.locators import base_page_locators
from test.UI.page_object.base_page import BasePage


class HomePage(BasePage):

    def click_forms_button(self):
        self.click(base_page_locators.FORMS_BUTTON, 10)
