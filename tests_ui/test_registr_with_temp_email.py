import time
import allure
import pytest
import requests
from pages.registration_page import RegistrationPage
from utils import generator
from utils.config import BasePageConfig
from utils.temp_email import create_temp_email, get_messages, read_message

@pytest.mark.parametrize('role', ['buyer', 'seller'])
def test_registration(page, role:str):
        registration_page = RegistrationPage(page)
        with allure.step('Open base url'):
            registration_page.open_page(BasePageConfig.base_url)
        with allure.step('Click on registration button'):
            registration_page.click_registration_button()
        if role == 'buyer':
            registration_page.click_be_buyer_button()
        elif role == 'seller':
            registration_page.click_be_seller_button()
        # Создание временной почты и заголовков
        email, headers = create_temp_email()
        with allure.step(f'Set email for registration: {email}'):
            registration_page.fill_login_field(email)
        password = generator.random_password()
        with allure.step(f'Fill password: {password}'):
            registration_page.fill_password_field(password)

        with allure.step('Click registration'):
            registration_page.click_start_buying_text()
            registration_page.click_create_account_button()

        message_id = None
        for _ in range(60):
            try:
                messages = get_messages(headers)
                if messages:
                    message_id = messages[0]['id']
                    break
            except requests.HTTPError as e:
                print(f"Ошибка API: {e}")
            time.sleep(1)

        assert message_id is not None, "Письмо с подтверждением не пришло"
        message = read_message(message_id, headers)
        print("Содержимое письма:", message)