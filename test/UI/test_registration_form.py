import allure
import pytest

from core.enums.gender import Gender
from core.enums.user import User
from test.UI.page_object.home_page import HomePage
from test.UI.page_object.forms_page import FormsPage


@pytest.mark.usefixtures("driver")
class TestStudentRegistration:

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name, last_name, gender,   phone", [
                            ("Olivia",    "Smith",   "Female", "1234567890"),
                            ("Oliver",    "Jones",   "Male",   "9876543210"),
                            ("Princes",   "George",  "Other",  "0147258369")])
    def test_student_registration_with_required_fields(self, first_name, last_name, gender, phone):
        home_page = HomePage(self.driver)
        forms_page = FormsPage(self.driver)
        user = User(first_name=first_name, last_name=last_name, gender=Gender(gender), phone=phone)
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.registrate_user(user)
        forms_page.click_submit_button()

    @allure.severity(allure.severity_level.NORMAL)
    def test_student_registration_form_required_fields(self):
        home_page = HomePage(self.driver)
        forms_page = FormsPage(self.driver)
        home_page.click_forms_button()
        forms_page.click_practice_form()
        forms_page.click_submit_button()
        assert forms_page.check_visibility_of_alert_symbol_on_first_name_field()
        assert forms_page.check_visibility_of_alert_symbol_on_last_name_field()
        assert forms_page.check_visibility_of_alert_symbol_on_mobile_field()
