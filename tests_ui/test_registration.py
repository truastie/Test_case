import allure
import pytest
from pytest_playwright.pytest_playwright import page

from clients.postrgess_client import PostgresClient
from pages.registration_page import RegistrationPage

from utils import generator
from utils.config import BasePageConfig



class TestRegistration:

    @allure.title('Positive Registration Test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('role', ['buyer', 'seller'])
    def test_registration(self, page, role: str):
        registration_page = RegistrationPage(page)
        with allure.step('Open base url'):
            registration_page.open_page(BasePageConfig.base_url)
        with allure.step('Click on registration button'):
            registration_page.click_registration_button()
        if role == 'buyer':
            registration_page.click_be_buyer_button()
        elif role == 'seller':
            registration_page.click_be_seller_button()
        with allure.step(f'Fill login field by data: {generator.random_email}'):
            registration_page.fill_login_field(generator.random_email())
        with allure.step(f'Fill password field by data: {generator.random_password}'):
            registration_page.fill_password_field(generator.random_password())
        with allure.step('Click on create account button'):
            registration_page.click_start_buying_text()
            registration_page.click_create_account_button()
        with allure.step('Check post registration message'):
            registration_page.check_post_registration_text()


class TestNegativeRegistration:

    @pytest.mark.negative
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['a', '@gmail.com', '2'])
    def test_negative_registration(self,page, email):
        registration_page = RegistrationPage(page)
        with allure.step('Open base url'):
            registration_page.open_page(BasePageConfig.base_url)
        with allure.step('Click on registration button'):
            registration_page.click_registration_button()
        with allure.step(f'Fill login field by data: {email}'):
            registration_page.fill_login_field(email)
        with allure.step(f'Fill password field by data: {generator.random_password()}'):
            registration_page.fill_password_field(generator.random_password())
        with allure.step('Check that email is invalid'):
            registration_page.check_text_is_visible()