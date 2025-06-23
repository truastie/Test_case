import allure
import pytest
from pages.adding_to_cart import AddCartPage
from utils.config import LoginPageConfig


@pytest.mark.positive
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Positive Adding Element to cart Test')
class TestAddingElement:
    def test_adding_cart(self, page):
        page = AddCartPage(page)
        with allure.step('Open login page'):
            page.open_page(LoginPageConfig.login_url)
        with allure.step(f'Fill login field with {LoginPageConfig.login_field}'):
            page.fill_login_field(LoginPageConfig.login_field)
        with allure.step(f'Fill password field with {LoginPageConfig.password_field}'):
            page.fill_password_field(LoginPageConfig.password_field)
        with allure.step('Click button Log In'):
            page.click_button_log_in()
        with allure.step('Check profile page'):
            page.check_profile_page()
        with allure.step('Click at the base page All Categories'):
            page.click_all_categories_button()
        with allure.step('Click clothes button'):
            page.click_clothes_button()
        with allure.step('Click sportswear button'):
            page.click_sportswear_button()
        with allure.step('Check opened page'):
            page.check_sportswear_page()
        with allure.step('Click on blank ares page'):
            page.click_on_blank_area()
        with allure.step('Click to choose of first element'):
            page.click_first_element()
        with allure.step('Click to choose size of element'):
            page.click_to_choose_size()
        with allure.step('Click Add Cart Button'):
            page.click_add_to_cart()
        with allure.step('Check that message is visible'):
            page.check_message()
        with allure.step('Open shopping cart'):
            page.go_to_shopping_cart()
        with allure.step('Check opened cart'):
            page.check_opened_shopping_cart()
        with allure.step('Check that adding element in cart is visible'):
            page.verify_product_in_cart()
