from selenium import webdriver
from pages.login_page import LoginPage
from test_data import VALID_PASSWORD, VALID_USERNAME, INVALID_PASSWORD, INVALID_USERNAME
from selenium.webdriver.chrome.options import Options


def test_valid_login():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)    

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.take_screenshot("valid_login_result")

        message = login_page.get_message()
        assert "You logged into a secure area" in message
        print("Valid login test passed. Message:", message.strip())
    finally:
        driver.quit()



def test_invalid_login():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        login_page.take_screenshot("invalid_login_result")

        message = login_page.get_message()
        assert "Your username is invalid" in message
        print("Invalid login test passed. Message:", message.strip())
    finally:
        driver.quit()


if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
