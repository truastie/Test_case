import allure
import pytest

from pages.login_page import LoginPage
from utils.config import LoginPageConfig

@pytest.mark.positive
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Positive Login Test')
class TestLogin:
    def test_login(self, page):
        log_page =LoginPage(page)
        with allure.step('Open login page'):
            log_page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {LoginPageConfig.login_field}'):
            log_page.fill_login_field(LoginPageConfig.login_field)
        with allure.step(f'Fill password field with {LoginPageConfig.password_field}'):
            log_page.fill_password_field(LoginPageConfig.password_field)
        with allure.step('Click button Log In'):
            log_page.click_button_log_in()
        with allure.step('Check profile page'):
            log_page.check_profile_page()


@pytest.mark.negative
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Negative Login Test')
class TestNegativeLogin:

    @pytest.mark.parametrize('email', ['a', '@gmail.com', '2'])
    def test_negative_login(self, page, email):
        log_page = LoginPage(page)
        with allure.step('Open login page'):
            log_page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {email}'):
            log_page.fill_login_field(email)
        with allure.step(f'Fill password field with {LoginPageConfig.password_field}'):
            log_page.fill_password_field(LoginPageConfig.password_field)
        with allure.step('Check that email is invalid'):
            log_page.check_invalid_email()

    @pytest.mark.parametrize('password', ['123', '1'])
    def test_negative_password(self, page, password):
        log_page = LoginPage(page)
        with allure.step('Open login page'):
            log_page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {LoginPageConfig.login_field}'):
            log_page.fill_login_field(LoginPageConfig.login_field)
        with allure.step(f'Fill password field with {password}'):
            log_page.fill_password_field(password)
        with allure.step('Check that password is invalid'):
            log_page.check_inv_password()
