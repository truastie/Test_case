import pytest

from utils.Client import Client
from utils.api_case import WebApi
from utils.config import LoginPageConfig, RegistrationPageConfig
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel


@pytest.mark.positive
@pytest.mark.API

class TestApi:

    def test_login(self):
        Client().login(request=LoginModel(
            email=LoginPageConfig.login_field,
            password=LoginPageConfig.password_field
        ), expected_model=LoginResponseModel(
            ok='true',
            result='true'
        ))

    def test_registr(self):
        Client().registration(request=RegisterModel(
            email=RegistrationPageConfig.REGISTR_FIELD,
            password=RegistrationPageConfig.PASSWORD_FIELD),
            expected_model=RegisterResponseModel(
            ok='true',
            result='true'
        ))

class TestApiNegative:
    @pytest.mark.negative

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, password):
        response = WebApi().login(LoginPageConfig.login_field, '')
        status_code = response[1]
        assert status_code == 403
        assert response[0]['detail'] == "Wrong email or password, maybe email was not confirmed or account was deleted?"