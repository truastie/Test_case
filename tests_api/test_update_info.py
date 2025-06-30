import allure
import pytest

from models.web_models import LoginModel, LoginResponseModel, PersonalInfoUpdate, PersonalInfoUpdateResponseModel
from utils import generator
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)
class TestInfoAUpdate:
    def test_info_update(self):
        random_name = generator.random_name()
        rand_last_name = generator.random_name()
        rand_num = generator.random_digits_name()

        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):

            # login_model = LoginModel(
            #     email=LoginPageConfig.login_field,
            #     password=LoginPageConfig.password_field)
            # client.login(
            #     login_model,
            #     expected_model=LoginResponseModel(
            #     ok=True,
            #     result=True))
            client = Client()
            client.session.cookies.set(
                'access_token_cookie',
                LoginPageConfig.token)
        with allure.step('Put new Personal Info'):
            request = PersonalInfoUpdate(
                first_name=random_name,
                last_name=rand_last_name,
                country_id=+7,
                phone_number=rand_num)

        with allure.step('Update Personal Info'):
            client.post_info_update(
                request=request,
                expected_model=PersonalInfoUpdateResponseModel(
                ok=True,
                result=True),
                status_code=200)