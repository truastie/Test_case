import allure
import pytest

from models.web_models import SupplierUpdateNotification, SupplierNotificationResponseModel
from utils.Client import Client
from utils.config import LoginPageConfig


@pytest.mark.positive
@pytest.mark.API
@allure.severity(allure.severity_level.CRITICAL)

class TestSupplierAddProduct:
    def test_supplier_adding_product(self):
        with allure.step(f"Log in with {LoginPageConfig.supplier_token}"):
            client = Client()
            print(f"Используем токен: {LoginPageConfig.supplier_token}")  # для отладки
            client.set_token = LoginPageConfig.supplier_token
            client.session.cookies.set('access_token_cookie', LoginPageConfig.supplier_token)
        with allure.step(f'Fill request'):
            request=SupplierUpdateNotification(
                on_advertising_campaigns= True,
                on_order_updates= True,
                on_order_reminders= True,
                on_product_updates= True,
                on_product_reminders= True,
                on_reviews_of_products= True,
                on_change_in_demand= True,
                on_advice_from_abra= True,
                on_account_support= True)

        with allure.step(f'Update Notifications'):
            client.post_supplier_notification(request=request,
                                            expected_model=SupplierNotificationResponseModel(ok=True, result=True),
                                            status_code=200)