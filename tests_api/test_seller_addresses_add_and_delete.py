import allure
import pytest

from models.web_models import SellerAddressRequestBody, SellerAddressRequest, SellerAddressPhoneRequest, \
    SellerAddressRequestResponseModel, SellerAddressResultModel, \
    DeleteSellerAddressResponse
from utils import generator
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)
class TestSellerAddressesAdd:
    def test_seller_adding_address(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            client = Client()
            client.session.cookies.set(
                'access_token_cookie',
                LoginPageConfig.token)
            rand_num=generator.random_digits_name(5)
            random_name=generator.random_name()
        with allure.step('Put new data'):
            request = SellerAddressRequestBody(
                seller_address_request=SellerAddressRequest(
                    is_main=False,
                    country_id=5,
                    first_name=random_name,
                    last_name=random_name,
                    city=random_name,
                    street=random_name,
                    building=rand_num,
                    apartment=rand_num,
                    postal_code='96075'),
                seller_address_phone_request=SellerAddressPhoneRequest(
                    country_id=5,
                    phone_number=rand_num))
        with allure.step('Update information'):
            client.post_sellers_adding_address(
                request=request,
                expected_model=SellerAddressRequestResponseModel(ok=True, result=(SellerAddressResultModel(id=1)),
                status_code=201))

    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Delete added address to seller')
    def test_delete_sellers_address(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            client = Client()
            client.session.cookies.set(
                'access_token_cookie',
                LoginPageConfig.token)
        with allure.step('Fill address_id and delete address'):
            client.delete_sellers_address(address_id=88,
                                          expected_model=DeleteSellerAddressResponse(ok=True, result=True),
                                          status_code=200)
