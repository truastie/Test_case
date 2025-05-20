import allure
import pytest

from pages.login_page import LoginPage
from utils.config import LoginPageConfig

@pytest.mark.positive

class TestLogin:
    def test_login(self, page):
        log_page =LoginPage(page)
        with allure.step('Open login page'):
            log_page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {LoginPageConfig.login_field}'):
            log_page.fill_login_field(LoginPageConfig.login_field)
        with allure.step(f'Fill password field with {LoginPageConfig.password_field}'):
            log_page.fill_password_field(LoginPageConfig.password_field)
        with allure.step('lick button Log In'):
            log_page.click_button_log_in()
        with allure.step('Check profile page'):
            log_page.check_profile_page()
