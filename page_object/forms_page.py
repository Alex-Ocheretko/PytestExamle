from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import forms_page_locators
from page_object.base_page import BasePage


class FormsPage(BasePage):

    # Student Registration Form
    def click_practice_form(self):
        self.click(forms_page_locators.PRACTICE_FORM, 10)

    def fill_first_name(self, first_name):
        self.send_keys(forms_page_locators.FIRST_NAME_FIELD, 10, first_name)

    def fill_last_name(self, last_name):
        self.send_keys(forms_page_locators.LAST_NAME_FIELD, 10, last_name)

    def enter_mobile_phone(self, phone):
        self.send_keys(forms_page_locators.PHONE_FIELD, 10, phone)

    def click_gender_male_radio_button(self):
        self.click(forms_page_locators.GENDER_MALE, 10)

    def click_gender_female_radio_button(self):
        self.click(forms_page_locators.GENDER_FEMALE, 10)

    def click_gender_other_radio_button(self):
        self.click(forms_page_locators.GENDER_OTHER, 10)

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(forms_page_locators.SUBMIT_BUTTON, 10)

    def check_visibility_of_alert_symbol_on_first_name_field(self):
        value = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(forms_page_locators.FIRST_NAME_FIELD)
        ).value_of_css_property("background-image")
        if value is not None:
            return True
        else:
            return False

    def check_visibility_of_alert_symbol_on_last_name_field(self):
        value = self.value_of_css_property(forms_page_locators.LAST_NAME_FIELD, 10, "background-image")
        if value is not None:
            return True
        else:
            return False

    def check_visibility_of_alert_symbol_on_mobile_field(self):
        value = self.value_of_css_property(forms_page_locators.PHONE_FIELD, 10, "background-image")
        if value is not None:
            return True
        else:
            return False

    def check_colour_of_gender_check_box(self):
        value = self.value_of_css_property(forms_page_locators.GENDER_MALE, 10, "color")
        if value == "rgba(33, 37, 41, 1)":
            return True
        else:
            return False

    # submitted data window
    def get_name_on_window_of_submitted_data(self):
        name = self.get_text(forms_page_locators.NAME_ON_WINDOW_OF_SUBMITTED_DATA, 10)
        return name

    def get_phone_on_window_of_submitted_data(self):
        phone = self.get_text(forms_page_locators.PHONE_ON_WINDOW_OF_SUBMITTED_DATA, 10)
        return phone

    def get_gender_on_window_of_submitted_data(self):
        gender = self.get_text(forms_page_locators.GENDER_ON_WINDOW_OF_SUBMITTED_DATA, 10)
        return gender
