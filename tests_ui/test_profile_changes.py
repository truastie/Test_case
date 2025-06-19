import allure
import pytest

from pages.profile_changes import ProfileChangesPage
from utils.config import LoginPageConfig
from utils.generator import random_name, random_digits_name


@pytest.mark.positive
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Positive Profile Changes Test')
class TestProfileChanges:
    def test_profile_changes(self, page):
        page=ProfileChangesPage(page)
        with allure.step('Open login page'):
            page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {LoginPageConfig.login_field}'):
            page.fill_login_field(LoginPageConfig.login_field)
        with allure.step(f'Fill password field with {LoginPageConfig.password_field}'):
            page.fill_password_field(LoginPageConfig.password_field)
        with allure.step('Click button Log In'):
            page.click_button_log_in()
        with allure.step('Check profile page'):
            page.check_profile_page()
        with allure.step('Click profile button'):
            page.click_button_profile()
        with allure.step('Click my profile'):
            page.click_my_profile()
        with allure.step('Fill new first name'):
            page.fill_first_name(random_name())
        with allure.step('Fill new last name'):
            page.fill_last_name(random_name())
        with allure.step('Fill new number'):
            page.fill_phone_number(random_digits_name())
        with allure.step('Click save button'):
            page.click_save_button()