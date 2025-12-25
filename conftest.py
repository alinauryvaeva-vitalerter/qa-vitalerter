import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    """
        Base fixture:
        - opens Chrome
        - maximizes window
        - closes browser after test
        """
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user_credentials():

    email = os.getenv("LOGIN_EMAIL")
    password = os.getenv("LOGIN_PASSWORD")

    if not email or not password:
        pytest.fail("LOGIN_EMAIL or LOGIN_PASSWORD not found in .env file")

    return {"email": email, "password": password}

@pytest.fixture(scope="function")
def logged_in_driver(driver, user_credentials):
    """
    Login fixture:
    - uses base driver
    - logs user into system
    - returns authorized driver
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_email(user_credentials["email"])
    login_page.enter_password(user_credentials["password"])

    assert login_page.is_logged_in(), "Failed to log in during fixture setup"

    return driver