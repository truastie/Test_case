import allure
import pytest

from utils.Client import Client
from utils.api_case import WebApi
from utils.config import LoginPageConfig, RegistrationPageConfig
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError


class TestApi:
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)

    def test_login(self):
        client=Client().login(request=LoginModel(
            email=LoginPageConfig.login_field,
            password=LoginPageConfig.password_field
        ), expected_model=LoginResponseModel(
            ok=True,
            result=True
        ))
        print(client)

    def test_registr(self):
        Client().registration(request=RegisterModel(
            email=RegistrationPageConfig.REGISTR_FIELD,
            password=RegistrationPageConfig.PASSWORD_FIELD),
            expected_model=RegisterResponseModel(
            ok=True,
            result=True
        ))


class TestApiNegative:
    @pytest.mark.negative
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, password:str):
        response = Client().login(
            request=LoginModel(email=LoginPageConfig.login_field, password=password),
            expected_model=ValidationError(),
            status_code=403
        )
        print(response)
