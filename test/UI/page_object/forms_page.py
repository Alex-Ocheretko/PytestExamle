from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.UI.locators import forms_page_locators
from test.UI.page_object.base_page import BasePage


class FormsPage(BasePage):

    # Student Registration Form
    def click_practice_form(self):
        self.click(forms_page_locators.PRACTICE_FORM)

    def fill_first_name(self, first_name):
        self.send_keys(forms_page_locators.FIRST_NAME_FIELD, first_name)

    def fill_last_name(self, last_name):
        self.send_keys(forms_page_locators.LAST_NAME_FIELD, last_name)

    def enter_mobile_phone(self, phone):
        self.send_keys(forms_page_locators.PHONE_FIELD, phone)

    def click_gender_radio_button(self, gender):
        self.click((By.XPATH, "//div[@id='genterWrapper']//input[@value='{}']/..".format(gender)))

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(forms_page_locators.SUBMIT_BUTTON)

    def check_visibility_of_alert_symbol_on_first_name_field(self):
        value = self.value_of_css_property(forms_page_locators.FIRST_NAME_FIELD, "background-image")
        if value:
            return True

    def check_visibility_of_alert_symbol_on_last_name_field(self):
        value = self.value_of_css_property(forms_page_locators.LAST_NAME_FIELD, "background-image")
        if value:
            return True

    def check_visibility_of_alert_symbol_on_mobile_field(self):
        value = self.value_of_css_property(forms_page_locators.PHONE_FIELD, "background-image")
        if value:
            return True

    # submitted data window
    def wait_until_submitted_data_window_opens(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(forms_page_locators.WINDOW_OF_SUBMITTED_DATA))

    def get_name_on_window_of_submitted_data(self):
        name = self.get_text(forms_page_locators.NAME_ON_WINDOW_OF_SUBMITTED_DATA)
        return name

    def get_phone_on_window_of_submitted_data(self):
        phone = self.get_text(forms_page_locators.PHONE_ON_WINDOW_OF_SUBMITTED_DATA)
        return phone

    def get_gender_on_window_of_submitted_data(self):
        gender = self.get_text(forms_page_locators.GENDER_ON_WINDOW_OF_SUBMITTED_DATA)
        return gender
