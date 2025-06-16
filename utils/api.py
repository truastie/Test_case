# import json
# import re
#
# import requests
#
# from utils import generator
#
#
# class WebApi:
#     def __init__(self):
#         self.base_url='https://dev.abra-market.com'
#
#
#     def login(self, request) -> json:
#         response = requests.post(self.base_url + '/auth/sign-in', data=json.dumps(request))
#         return response.json(), response.status_code
#
#     def registration(self, request) -> json:
#         response = requests.post(self.base_url + '/auth/sign-up/supplier', data=json.dumps(request))
#         return response.json(), response.status_code
# #

import json
import time

import allure
import requests
import re
from playwright.sync_api import expect

from cloudscraper import session

from utils import generator
from utils.config import LoginPageConfig

# import temp_mails
# from temp_mails import Tenminemail_com



class AbraApi:
    def __init__(self):
        self.base_url = 'https://api.dev.abra-market.com/'
        self.session = requests.Session()
        # создаем обьект сессии


    def login(self, email: str, password: str) -> None:
        data = {
            'email': email,
            'password': password
        }
        self.session = requests.Session()
        response = self.session.post(self.base_url + 'auth/sign-in', json=data)
        response.raise_for_status()
        # тут сохраняется токен - session.post


    def update_password(self, old_password: str, new_password: str) -> json:
        data = {
                "old_password": old_password,
                "new_password": new_password
        }

        response = self.session.post(self.base_url + 'users/password/change', json=data)
        response.raise_for_status()
        print({'old_password' : old_password, 'new_password' : new_password})


class EmailConfirmation(AbraApi):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        self.email_url = 'https://api.internal.temp-mail.io/api/v3/email/'


    def register_supplier(self) -> json:
        password = generator.random_password()
        data = {'email': 'eit7dqbw8z@qzueos.com.com',
                'password': password
                }
        res = requests.post(self.base_url + 'auth/sign-up/supplier', data=json.dumps(data))
        return res.json(), res.status_code


    def get_token_from_email(self):
        response = requests.get(self.email_url + 'eit7dqbw8z@qzueos.com/' + 'messages')
        data = response.json()
        email_data = data[0]['body_text']
        token_pattern = r'token=([a-zA-Z0-9.,;!?@#$%^&*_+=()-]+)'
        token = re.findall(token_pattern, email_data)
        clean_token = token[0]
        print(clean_token)
        return clean_token

    def confirm_email(self):
        clean_token = self.get_token_from_email()
        response = requests.get(self.base_url + f'/auth/sign-up/confirmEmail?token={clean_token}', json=clean_token)
        print(self.base_url + f'/auth/sign-up/confirmEmail?token={clean_token}')
        print(response.text)

class ConfirmTempmail(AbraApi):
    def __init__(self, timeout=5000):
        super().__init__()
        self.session = requests.Session()
        self.timeout = timeout
        self.base_url = 'https://api.internal.temp-mail.io/api/v3/email/'
        self.email_url = 'https://tempmail.plus/'
        self.email_first_part = generator.random_name(10)
        self.first_id = None
        self.url_from_email = None

    # РЕГИСТРАЦИЯ НА САЙТЕ https://tempmail.plus/
    def register_user(self, user_type) -> json:
        password = generator.random_password()
        data = {'email': f'{self.email_first_part}@fexbox.org',
                'password': password
                }
        self.session.post(self.base_url + f'auth/sign-up/{user_type}', json=data)
        response = self.session.get(
            url=f'{self.email_url}api/mails?email={self.email_first_part}%40fexbox.org&first_id=0&epin=')
        return data.get('email'), response.json(), response.status_code

    def get_id_from_email(self):
        response = self.session.get(
            url=f'{self.email_url}api/mails?email={self.email_first_part}%40fexbox.org&limit=20&epin=')
        data = response.json()
        self.email_id = data.get('first_id')
        print(data)
        return self.email_id

    # РЕГИСТРАЙИЯ НА САЙТЕ https://tempmail.plus/

    # 1 шаг инициализация ящика: пустой ящик, проверяем его наличие, получаем response с нулевыми значениями
    def check_email_exists(self):
        data = {'email': f'{self.email_first_part}@fexbox.org'
                }
        response = self.session.get(
            url=f'{self.email_url}api/mails?email={self.email_first_part}%40fexbox.org&limit=20&epin=')
        return data.get('email'), response.status_code


    # 2 шаг ожидание письма: ящик постоянно обновляется и проверяет, пришло ли письмо, повторяется много раз, пока не придет письмо
    # сначала response везде по нулям, когда пришло письмо, то там подробная инфа об отправителе
    def check_mailbox(self):
        while True:
            response = self.session.get(
                url=f'{self.email_url}api/mails?email={self.email_first_part}%40fexbox.org&first_id=0&epin=')
            data = response.json()
            self.first_id = data['first_id']
            if self.first_id != 0:
                return self.first_id
            time.sleep(5)

    # 3 шаг подтверждение получения письма: в response есть first_id и информация об отправителе, остальное по нулям
    def get_email_content(self):
        if self.first_id:
            print(f"Получен first_id: {self.first_id}")
        else:
            print("first_id еще не получен!")

        response = self.session.get(
            url=f'{self.email_url}api/mails?email={self.email_first_part}%40fexbox.org&first_id={self.first_id}&epin=')
        return response

    # 4 шаг : полное содержимое письма, включая url и токен для подтверждения регистрации
    def get_confirm_link_from_email(self):
        if self.first_id:
            print(f"Получен first_id: {self.first_id}")
        else:
            print("first_id еще не получен!")
        response = self.session.get(url=f'{self.email_url}api/mails/{self.first_id}?email={self.email_first_part}%40fexbox.org&epin=')
        data = response.json()
        email_data = data["text"]
        url_pattern = r"(https://dev\.abra-market\.com/register/confirm_email\?token=[a-zA-Z0-9.,;!?@#$%^&*_+=()-]+)"
        self.url_from_email = re.findall(url_pattern, email_data)
        return self.url_from_email