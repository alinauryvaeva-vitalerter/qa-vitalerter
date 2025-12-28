from pages.login_page import LoginPage


def test_login_with_wrong_email(driver, base_url, invalid_user_credentials):
    login_page = LoginPage(driver, base_url)
    login_page.open()

    login_page.enter_email(invalid_user_credentials["email"])
    login_page.click_next()

    # пароль НЕ должен появиться
    assert not login_page.is_password_input_visible()
    assert login_page.is_still_on_login_page()
