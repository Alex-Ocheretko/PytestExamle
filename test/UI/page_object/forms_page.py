from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.decorators import handle_none_argument
from core.enums.hobby import Hobby
from core.enums.user import User
from test.UI.page_object.base_page import BasePage
from utils.base_utils import DEFAULT_EXPLICIT_WAIT


class FormsPage(BasePage):
    PRACTICE_FORM = (By.XPATH, "//span[text()='Practice Form']")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    PHONE_FIELD = (By.CSS_SELECTOR, "#userNumber")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")
    GENDER_RADIO_BUTTON = (By.XPATH, "//div[@id='genterWrapper']//input[@value='{}']/..")
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_FIELD = (By.CSS_SELECTOR, "#subjectsContainer")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    HOBBY_CHECKBOX = (By.XPATH, "//label[contains(@for,'hobbies-checkbox-') and contains(text(), '{}')]")
    CURRENT_ADDRESS_FIELD = (By.XPATH, "//textarea[@placeholder='Current Address']")

    WINDOW_OF_SUBMITTED_DATA = (By.XPATH, "//div[text()='Thanks for submitting the form']")

    # Student Registration Form
    def registrate_user(self, user: User):
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_email(user.email)
        self.click_gender_radio_button(user.gender)
        self.enter_mobile_phone(user.phone)
        self.enter_date_of_birth(user.date_of_birth)
        self.enter_subjects(user.subjects)
        self.click_hobby(user.hobbies)
        self.enter_current_address(user.current_address)
        self.enter_state(user.state)
        self.enter_city(user.state)

    def click_practice_form(self):
        self.click(self.PRACTICE_FORM)

    def enter_first_name(self, first_name: str):
        self.send_keys(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name: str):
        self.send_keys(self.LAST_NAME_FIELD, last_name)

    @handle_none_argument
    def enter_email(self, email: str):
        self.send_keys(self.EMAIL_FIELD, email)

    def click_gender_radio_button(self, gender: str):
        self.click(self.replace_placeholders_in_locator(self.GENDER_RADIO_BUTTON, gender))

    def enter_mobile_phone(self, phone: str):
        self.send_keys(self.PHONE_FIELD, phone)

    @handle_none_argument
    def enter_date_of_birth(self, date_of_birth: str):
        self.send_keys(self.DATE_OF_BIRTH_FIELD, date_of_birth)

    @handle_none_argument
    def enter_subjects(self, subjects: str):
        self.send_keys(self.SUBJECTS_FIELD, subjects)

    @handle_none_argument
    def click_hobby(self, hobbies: List[Hobby]):
        for hobby in hobbies:
            self.click(self.replace_placeholders_in_locator(self.HOBBY_CHECKBOX, hobby))

    @handle_none_argument
    def enter_current_address(self, address: str):
        self.send_keys(self.CURRENT_ADDRESS_FIELD, address)

    @handle_none_argument
    def enter_state(self, state):
        pass

    @handle_none_argument
    def enter_city(self, city):
        pass

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(self.SUBMIT_BUTTON)
        self.wait_until_submitted_data_window_opens()

    def check_visibility_of_alert_symbol_on_first_name_field(self) -> bool:
        value = self.value_of_css_property(self.FIRST_NAME_FIELD, "background-image")
        if value:
            return True

    def check_visibility_of_alert_symbol_on_last_name_field(self) -> bool:
        value = self.value_of_css_property(self.LAST_NAME_FIELD, "background-image")
        if value:
            return True

    def check_visibility_of_alert_symbol_on_mobile_field(self) -> bool:
        value = self.value_of_css_property(self.PHONE_FIELD, "background-image")
        if value:
            return True

    # submitted data window
    def wait_until_submitted_data_window_opens(self):
        WebDriverWait(self.driver, DEFAULT_EXPLICIT_WAIT).until(
            EC.presence_of_element_located(self.WINDOW_OF_SUBMITTED_DATA))

    class SubmittedDataForm:

        VALUE_FIELD = (By.XPATH, "//td[text()='{}']/following-sibling::td")

        def get_value_by_label(self, label: str) -> str:
            return self.get_text(self, self.replace_placeholders_in_locator(self.VALUE_FIELD, label))
