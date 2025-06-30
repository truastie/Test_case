import allure
import pytest

from models.web_models import AddingElementtoFavModel, AddingElementtoFavResponseModel
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)

class TestFavorites:
    def test_adding_element_to_fav(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            client = Client()
            client.session.cookies.set(
                'access_token_cookie',
                LoginPageConfig.token)
        with allure.step('Choose product_id'):
            request=AddingElementtoFavModel(product_id=1774)
        with allure.step('Adding Element to fav'):
            client.post_adding_element_to_fav(request=request, expected_model=AddingElementtoFavResponseModel(ok=True, result=True),
                                              status_code=200)