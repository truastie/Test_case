import allure
import pytest

from models.web_models import SellerAddressRequest, SellerAddressRequestResponseModel, LoginModel, LoginResponseModel
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
            # client.session.cookies.set(
            #     'access_token_cookie',
            #     'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwMywiaWF0IjoxNzUwOTU1MDYwLCJuYmYiOjE3NTA5NTUwNjAsImp0aSI6IjdlZmRhMDYwLWFjNzYtNGJlNS05Y2M5LWYzMGY3MTgyNzJiNCIsImV4cCI6MTc1MTU1OTg2MCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.VGLyuCPLlE4iKuytfntoPWPTwVqfS5IeiQyUo7aEoaM'
            # )
            client.set_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwMywiaWF0IjoxNzUwOTU1MDYwLCJuYmYiOjE3NTA5NTUwNjAsImp0aSI6IjdlZmRhMDYwLWFjNzYtNGJlNS05Y2M5LWYzMGY3MTgyNzJiNCIsImV4cCI6MTc1MTU1OTg2MCwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.VGLyuCPLlE4iKuytfntoPWPTwVqfS5IeiQyUo7aEoaM')
        random_name = generator.random_name()
        rand_num = generator.random_digits_name()
        with allure.step('Put new data'):
            request = SellerAddressRequest(
                is_main=False,
                country_id=1,
                first_name=random_name,
                last_name=random_name,
                postal_code=rand_num)

        with allure.step('Update information'):
            client.post_sellers_adding_address(request=request,
                                             expected_model=SellerAddressRequestResponseModel(
                                                 ok=True,
                                                id=1),
                                             status_code=201)

