import allure
import pytest

from models.web_models import SellerAddressRequest, SellerAddressRequestResponseModel, LoginModel, LoginResponseModel, \
    SellerAddressRequestBody, SellerAddressPhoneRequest
from utils import generator
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)
class TestAddresses:
    def test_seller_adding_address(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            client = Client()
            client.session.cookies.set(
                'access_token_cookie',
                LoginPageConfig.token)
        random_name = generator.random_name()
        rand_num = generator.random_digits_name()
        with allure.step('Put new data'):
            request = SellerAddressRequestBody(
                seller_address_request=SellerAddressRequest(
                    is_main=False,
                    country_id=1,
                    first_name=random_name,
                    last_name=random_name,
                    city='Warsaw',
                    street=random_name,
                    building=rand_num,
                    apartment=rand_num,
                    postal_code=rand_num),
                seller_address_phone_request=SellerAddressPhoneRequest(
                    country_id=1,
                    phone_number=rand_num))

        with allure.step('Update information'):
            client.post_sellers_adding_address(
                request=request,
                expected_model=SellerAddressRequestResponseModel(ok=True),
                status_code=201)
