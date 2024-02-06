from typing import List

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.decorators import handle_none_argument
from core.enums.hobby import Hobby
from core.enums.user import User, convert_user_object_to_dict
from test.UI.page_object.base_page import BasePage
from core.constants import DEFAULT_EXPLICIT_WAIT
from utils.string_utils import replace_placeholders_in_locator


class FormsPage(BasePage):
    PRACTICE_FORM = (By.XPATH, "//span[text()='Practice Form']")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    PHONE_FIELD = (By.CSS_SELECTOR, "#userNumber")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")
    GENDER_RADIO_BUTTON = (By.XPATH, "//div[@id='genterWrapper']//input[@value='{}']/..")
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_FIELD = (By.CSS_SELECTOR, "#subjectsContainer input")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    HOBBY_CHECKBOX = (By.XPATH, "//label[contains(@for,'hobbies-checkbox-') and contains(text(), '{}')]")
    CURRENT_ADDRESS_FIELD = (By.XPATH, "//textarea[@placeholder='Current Address']")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, "#state")
    DROP_DOWN_PARAMETERS = (By.XPATH, "//div[text()='{}']")
    CITY_DROP_DOWN = (By.CSS_SELECTOR, "#city")

    def register_user(self, user: User):
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
        self.enter_city(user.city)

    def click_practice_form(self) -> None:
        self.click(self.PRACTICE_FORM)

    def enter_first_name(self, first_name: str) -> None:
        self.send_keys(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.send_keys(self.LAST_NAME_FIELD, last_name)

    @handle_none_argument
    def enter_email(self, email: str) -> None:
        self.send_keys(self.EMAIL_FIELD, email)

    def click_gender_radio_button(self, gender: str) -> None:
        self.click(replace_placeholders_in_locator(self.GENDER_RADIO_BUTTON, gender))

    def enter_mobile_phone(self, phone: str) -> None:
        self.send_keys(self.PHONE_FIELD, phone)

    @handle_none_argument
    def enter_date_of_birth(self, date_of_birth: str) -> None:
        self.send_keys(self.DATE_OF_BIRTH_FIELD, date_of_birth)
        self.send_keys(self.DATE_OF_BIRTH_FIELD, Keys.ENTER)

    @handle_none_argument
    def enter_subjects(self, subjects: List[str]) -> None:
        for subject in subjects:
            self.send_keys(self.SUBJECTS_FIELD, subject)
            self.send_keys(self.SUBJECTS_FIELD, Keys.ENTER)

    @handle_none_argument
    def click_hobby(self, hobbies: List[Hobby]) -> None:
        for hobby in hobbies:
            self.click(replace_placeholders_in_locator(self.HOBBY_CHECKBOX, hobby))

    @handle_none_argument
    def enter_current_address(self, address: str) -> None:
        self.send_keys(self.CURRENT_ADDRESS_FIELD, address)

    @handle_none_argument
    def enter_state(self, state) -> None:
        self.click(self.STATE_DROP_DOWN)
        self.click(replace_placeholders_in_locator(self.DROP_DOWN_PARAMETERS, state))

    @handle_none_argument
    def enter_city(self, city) -> None:
        self.click(self.CITY_DROP_DOWN)
        self.click(replace_placeholders_in_locator(self.DROP_DOWN_PARAMETERS, city))

    def click_submit_button(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(self.SUBMIT_BUTTON)

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

    class SubmittedDataForm(BasePage):

        WINDOW_OF_SUBMITTED_DATA = (By.XPATH, "//div[text()='Thanks for submitting the form']")
        VALUE_FIELD = (By.XPATH, "//td[text()='{}']/following-sibling::td")

        labels = {"student_name": "Student Name",
                  "phone": "Mobile",
                  "gender": "Gender",
                  "email": "Student Email",
                  "date_of_birth": "Date of Birth",
                  "subjects": "Subjects",
                  "hobbies": "Hobbies",
                  "current_address": "Address",
                  "state_and_city": "State and City"}

        def get_value_by_label(self, label: str) -> str:
            return self.get_text(replace_placeholders_in_locator(self.VALUE_FIELD, self.labels[label]))

        def check_student_data(self, user: User) -> dict[str, bool]:
            result = {}
            expected_date = convert_user_object_to_dict(user)
            for kay, value in expected_date.items():
                if value:
                    result[kay] = self.get_value_by_label(kay) == value
            return result

        def wait_for_shown(self) -> None:
            WebDriverWait(self.driver, DEFAULT_EXPLICIT_WAIT).until(
                EC.presence_of_element_located(self.WINDOW_OF_SUBMITTED_DATA))
