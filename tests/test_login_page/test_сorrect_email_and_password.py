import pytest
from pages.login_page import LoginPage


def test_login_positive(driver, user_credentials):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_email(user_credentials["email"])
    login_page.enter_password(user_credentials["password"])
    login_page.click_login()

    # Проверка (замени на актуальный селектор после логина)
    assert "login" not in driver.current_url.lower()