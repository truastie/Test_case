import allure
import pytest

from clients.postrgess_client import PostgresClient
from utils import generator
from utils.Client import Client
from utils.api import ConfirmTempmail, EmailConfirmation
from utils.config import LoginPageConfig
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError


class TestApi:
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)

    def test_login(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            login_model=LoginModel(
                email=LoginPageConfig.login_field,
                password=LoginPageConfig.password_field)
        with allure.step(f'Log in by models {login_model} and {LoginResponseModel}'):
            response= Client().login(request=login_model,
                                    expected_model=LoginResponseModel(
                                    ok=True,
                                    result=True
            )
        )
        PostgresClient().get_user(LoginPageConfig.login_field, False, True)

    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('user_type', ['seller', 'supplier'])
    def test_registr(self, user_type: str):
        random_email = generator.random_email()
        random_password = generator.random_password()
        with allure.step(f'Registration by {random_email} and {random_password}'):
            registr_model=RegisterModel(
            email=random_email,
            password=random_password)
        with allure.step(f'Create user by {registr_model} and {RegisterResponseModel}'):
            Client().registration(request=registr_model,
                                  expected_model=RegisterResponseModel(
                                    ok=True,
                                    result=True),
                                  user_type=user_type)
        PostgresClient().get_user(random_email, False, False)



class TestApiNegative:
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['', '123', '@mail,r', '@gmail.ru'])
    @pytest.mark.parametrize('password', ['', '123'])

    def test_login_incorrect_data(self, email:str, password:str):
        response = Client().login(
            request=LoginModel(email=email, password=password),
            expected_model=ValidationError(),
            status_code=422
        )
        return response

class TestRegistrationApiAbra:
    @allure.title("Test register user and confirm email")
    def test_register_user_user_api(self):
        ConfirmTempmail().register_user('seller')
        ConfirmTempmail().check_email_exists()
        ConfirmTempmail().check_mailbox()
        ConfirmTempmail().get_email_content()


    @allure.title("Test register  and confirm email")
    def test_register_seller_user_api(self):
        EmailConfirmation().register_supplier()
        EmailConfirmation().get_token_from_email()
        EmailConfirmation().confirm_email()


