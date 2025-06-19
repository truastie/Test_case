from pages.base_page import BasePage
from playwright.sync_api import expect

class ProfileChangesPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.BUTTON_LOG_IN=self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.BUTTON_PROFILE=self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/button')
        self.MY_PROFILE=self.page.locator('//*[@id="header-popup"]/li[1]/a')
        self.CHANGE_FIRST_NAME=self.page.locator('//*[@id="firstName"]')
        self.CHANGE_LAST_NAME=self.page.locator('//*[@id="lastName"]')
        self.PUT_PHONE_NUMBER=self.page.locator('//*[@id="root"]/div/div/main/div/div/div[1]/form/fieldset/div[2]/label/div/input')
        self.SAVE_BUTTON=self.page.locator('//*[@id="root"]/div/div/main/div/div/div[1]/form/button')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)

    def click_button_log_in(self):
        self.LOGIN_FIELD.click(timeout=self.timeout)
        self.BUTTON_LOG_IN.click(timeout=self.timeout)

    def check_profile_page(self):
        expect(self.page).to_have_url('https://dev.abra-market.com/', timeout=self.timeout)

    def click_button_profile(self):
        self.BUTTON_PROFILE.click(timeout=self.timeout)

    def click_my_profile(self):
        self.MY_PROFILE.click(timeout=30000)

    def fill_first_name(self, name):
        self.CHANGE_FIRST_NAME.fill(name, timeout=self.timeout)

    def fill_last_name(self, last_name):
        self.CHANGE_LAST_NAME.fill(last_name,timeout=self.timeout)

    def fill_phone_number(self, number):
        self.PUT_PHONE_NUMBER.fill(number, timeout=self.timeout)

    def click_save_button(self):
        self.SAVE_BUTTON.click()