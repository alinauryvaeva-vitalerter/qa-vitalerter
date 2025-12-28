import pytest
from selenium.webdriver.common.by import By


def test_login_positive(driver, user_credentials):
    driver.get("https://app.vitalerter.com/login")

    # Используем данные из фикстуры user_credentials
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(user_credentials["email"])

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(user_credentials["password"])

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Добавь проверку успешного входа (assert)
    assert "dashboard" in driver.current_url.lower()