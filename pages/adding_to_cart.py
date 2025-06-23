from playwright.sync_api import expect
from pages.base_page import BasePage

class AddCartPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.BUTTON_LOG_IN=self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.ALL_CATEGORIES_BUTTON=self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[1]/button')
        self.CLOTHES_BUTTON=self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[1]/div/ul/li[2]/button')
        self.CHOOSE_CATEGORIES=self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[1]/div/div/li[1]/a[3]/div')
        self.CHOOSE_FIRST_ELEMENT=self.page.locator('//*[@id="root"]/div/div/main/div/div[2]/div[2]/article[1]/a/div[1]/div[2]')
        self.CHOOSE_SIZE=self.page.locator('//*[@id="root"]/div/div/main/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/button[1]')
        self.ADD_TO_CART=self.page.locator('//*[@id="root"]/div/div/main/div/div/div[2]/div[3]/div[1]/button[2]')
        self.MESSAGE_CHECK=self.page.get_by_text('Product has been added to cart')
        self.GO_TO_CART=self.page.get_by_text('Go to Shopping cart')
        self.product_title_locator = self.page.get_by_text('Martinez, Rowe and Peterson')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password,timeout=self.timeout)

    def click_button_log_in(self):
        self.LOGIN_FIELD.click(timeout=self.timeout)
        self.BUTTON_LOG_IN.click(timeout=self.timeout)

    def check_profile_page(self):
        expect(self.page).to_have_url('https://dev.abra-market.com/', timeout=self.timeout)

    def click_all_categories_button(self):
        self.ALL_CATEGORIES_BUTTON.click(timeout=self.timeout)

    def click_clothes_button(self):
        self.CLOTHES_BUTTON.click(timeout=self.timeout)

    def click_sportswear_button(self):
        self.CHOOSE_CATEGORIES.click(timeout=self.timeout)

    def check_sportswear_page(self):
        expect(self.page).to_have_url('https://dev.abra-market.com/products_list?category_id=4', timeout=self.timeout)

    def click_on_blank_area(self, x=10, y=10):
        # x,y — координаты для клика, чтобы пропала иконка
        self.page.mouse.click(x, y)

    def click_first_element(self):
        self.CHOOSE_FIRST_ELEMENT.click(timeout=self.timeout)

    def click_to_choose_size(self):
        expect(self.CHOOSE_SIZE).to_be_visible(timeout=self.timeout)
        expect(self.CHOOSE_SIZE).to_be_enabled(timeout=self.timeout)
        self.CHOOSE_SIZE.click()

    def click_add_to_cart(self):
        self.ADD_TO_CART.click(timeout=self.timeout)

    def check_message(self):
        expect(self.MESSAGE_CHECK).to_be_visible(timeout=self.timeout)

    def go_to_shopping_cart(self):
        self.GO_TO_CART.click(timeout=self.timeout)

    def check_opened_shopping_cart(self):
        expect(self.page).to_have_url('https://dev.abra-market.com/cart', timeout=self.timeout)

    def verify_product_in_cart(self):
        expect(self.product_title_locator).to_be_visible()
