import random
import string

import allure
import pytest

from page_object.home_page import HomePage
from page_object.forms_page import FormsPage


@pytest.mark.usefixtures("driver")
class TestFirst:

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name, last_name, gender", [("Olivia", "Smith", "Female"),
                                                               ("Oliver", "Jones", "Male"),
                                                               ("Princes", "George", "Other")])
    def test_student_registration_form(self, first_name, last_name, gender):
        home_page = HomePage(self.driver)
        forms_page = FormsPage(self.driver)
        phone = "".join(random.sample(string.digits, 10))
        home_page.close_fixedban_if_visible()
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.fill_first_name(first_name)
        forms_page.fill_last_name(last_name)
        forms_page.enter_mobile_phone(phone)
        if gender == "Male":
            forms_page.click_gender_male_radio_button()
        if gender == "Female":
            forms_page.click_gender_female_radio_button()
        if gender == "Other":
            forms_page.click_gender_other_radio_button()
        forms_page.click_submit_button()
        assert forms_page.get_name_on_window_of_submitted_data() == f"{first_name} {last_name}"
        assert forms_page.get_phone_on_window_of_submitted_data() == phone
        assert forms_page.get_gender_on_window_of_submitted_data() == gender

    @allure.severity(allure.severity_level.NORMAL)
    def test_student_registration_form_requirement_fields(self):
        home_page = HomePage(self.driver)
        forms_page = FormsPage(self.driver)
        home_page.close_fixedban_if_visible()
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.click_submit_button()
        assert forms_page.check_visibility_of_alert_symbol_on_first_name_field()
        assert forms_page.check_visibility_of_alert_symbol_on_last_name_field()
        assert forms_page.check_visibility_of_alert_symbol_on_mobile_field()
        assert forms_page.check_colour_of_gender_check_box()
