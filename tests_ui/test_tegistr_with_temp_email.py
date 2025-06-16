from datetime import time
import re

import allure
import pytest
from playwright.async_api import expect

from pages.registration_page import RegistrationPage
from utils import generator
from utils.config import BasePageConfig
from utils.temp_email import generate_random_email, get_messages, read_message

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
    login, email = generate_random_email()
    with allure.step(f'Set email for registration: {email}'):
        registration_page.fill_login_field(email)
    password = generator.random_password()
    with allure.step(f'Fill {password}'):
        registration_page.fill_password_field(password)
    with allure.step('Click registration'):
        registration_page.click_start_buying_text()
        registration_page.click_create_account_button()

    message_id = None
    for _ in range(60):
        messages = get_messages(login)
        if messages:
            message_id = messages[0]['id']
            break
        time.sleep(2)

    assert message_id is not None, "Письмо с подтверждением не пришло"

    message = read_message(login, message_id)
    body = message['body']

    match = re.search(r'https://dev\.abra-market\.com/register/confirm_email\?token=([a-zA-Z0-9_\-\.]+)', body)
    assert match, "Ссылка для подтверждения не найдена в письме"

    confirm_url = f"https://dev.abra-market.com/register/confirm_email?token={match.group(1)}"

    with allure.step('Переход по ссылке подтверждения'):
        page.goto(confirm_url)
        expect(page).to_have_content('A link for sign up has been sent to your email address.', timeout=10000)