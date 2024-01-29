import allure
import pytest

from core.enums.gender import Gender
from core.enums.user import User
from test.UI.page_object.home_page import HomePage
from test.UI.page_object.forms_page import FormsPage


class TestStudentRegistration:

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name, last_name, gender,   phone", [
        ("Olivia", "Smith", "Female", "1234567890"),
        ("Oliver", "Jones", "Male", "9876543210"),
        ("Princes", "George", "Other", "0147258369")])
    def test_student_registration_with_required_fields(self, driver, first_name, last_name, gender, phone):
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        submitted_data_form = forms_page.SubmittedDataForm(driver)
        user = User(first_name=first_name, last_name=last_name, gender=Gender(gender), phone=phone)
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.registrate_user(user)
        forms_page.click_submit_button()
        forms_page.wait_until_submitted_data_window_opens()
        assert submitted_data_form.check_student_data(user), "Some data have not been displayed on submitted data form."

    @allure.severity(allure.severity_level.NORMAL)
    def test_student_registration_form_required_fields(self, driver):
        home_page = HomePage(driver)
        forms_page = FormsPage(driver)
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.click_submit_button()
        assert forms_page.check_visibility_of_alert_symbol_on_first_name_field(), ""
        assert forms_page.check_visibility_of_alert_symbol_on_last_name_field()
        assert forms_page.check_visibility_of_alert_symbol_on_mobile_field()
