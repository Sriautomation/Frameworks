from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MESSAGE_BANNER = (By.ID, "flash")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.type_text(self.USERNAME, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_message(self):
        return self.get_text(self.MESSAGE_BANNER)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self.get_message()
