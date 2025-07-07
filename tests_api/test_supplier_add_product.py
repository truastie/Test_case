import allure
import pytest

from models.web_models import SupplierProductAddModel, SupplierProductAddResponseModel
from utils import generator
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)

class TestSupplierAddProduct:
    def test_supplier_adding_product(self):
        with allure.step(f"Log in with {LoginPageConfig.login_field} and {LoginPageConfig.password_field}"):
            client = Client()
            client.session.cookies.set(
             'access_token_cookie',
                LoginPageConfig.supplier_token)
        random_name = generator.random_name()
        with allure.step('Fill new product'):
            request=SupplierProductAddModel(
                name= random_name,
                description= random_name,
                brand=21,
                category=5)

        with allure.step('Add new product'):
            client.post_supplier_add_product(request=request, expected_model=SupplierProductAddResponseModel(ok=True),
                                             status_code=200)
