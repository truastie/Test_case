import allure
import pytest

from clients.postrgess_client import PostgresClient
from models.postgress_model import UserModel
from utils import generator
from utils.Client import Client
from utils.common_checker import check_difference_between_objects
from utils.config import LoginPageConfig
from models.web_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, ValidationError


class TestApi:
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)

    def test_login(self):
        response = Client().login(
            request=LoginModel(
                email=LoginPageConfig.login_field,
                password=LoginPageConfig.password_field
            ),
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

        Client().registration(request=RegisterModel(
            email=random_email,
            password=random_password),
            expected_model=RegisterResponseModel(
            ok=True,
            result=True
        ),
        user_type=user_type
        )
        PostgresClient().user_registration(random_email, False, False)



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

