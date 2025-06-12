from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.BUTTON_LOG_IN=self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.INVALID_EMAIL = self.page.get_by_text('Invalid email')
        self.INV_PASSWORD=self.page.get_by_text('Password must be at least 8 characters')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password,timeout=self.timeout)

    def click_button_log_in(self):
        self.LOGIN_FIELD.click(timeout=self.timeout)
        self.BUTTON_LOG_IN.click(timeout=self.timeout)

    def check_profile_page(self):
        expect(self.page).to_have_url('https://dev.abra-market.com/', timeout=self.timeout)

    def check_invalid_email(self):
        expect(self.INVALID_EMAIL).to_be_visible(timeout=self.timeout)

    def check_inv_password(self):
        expect(self.INV_PASSWORD).to_be_visible(timeout=self.timeout)

